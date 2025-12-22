#!/usr/bin/env python
from __future__ import annotations

import argparse
import pathlib
import sys

try:
    from emu_runner import (
        assemble_source,
        load_program,
        read_u16,
        run_until_ret,
        write_u16,
    )
except ModuleNotFoundError:
    skill_scripts = pathlib.Path(
        "C:/Users/Grimakis/.codex/skills/tandy-m100-programming/scripts"
    )
    sys.path.insert(0, str(skill_scripts))
    from emu_runner import (
        assemble_source,
        load_program,
        read_u16,
        run_until_ret,
        write_u16,
    )


def _cell_addr(base: int, row: int, col: int) -> int:
    return base + ((col * 10) + row) * 2


def _fill_array(cpu, base: int, rows: int, cols: int, val: int) -> None:
    for r in range(rows):
        for c in range(cols):
            write_u16(cpu, _cell_addr(base, r, c), val)


def _set_obstacles(cpu, base: int, cells: list[tuple[int, int]]) -> None:
    for r, c in cells:
        addr = _cell_addr(base, r, c)
        val = read_u16(cpu, addr)
        write_u16(cpu, addr, (val & 0xFF) | 0x0100)


def _expect_eq(label: str, got: int, want: int) -> None:
    if got != want:
        raise SystemExit(f"{label}: expected {want}, got {got}")


def _setup_mp(cpu, mp_addr: int, s_base: int) -> None:
    write_u16(cpu, mp_addr, s_base)
    write_u16(cpu, mp_addr + 2, 0)


def _run_fill_test(cpu, mp_addr: int, s_base: int) -> None:
    cpu.A.value = 0
    cpu.H.value = (mp_addr >> 8) & 0xFF
    cpu.L.value = mp_addr & 0xFF
    run_until_ret(cpu)

    for r in range(1, 9):
        for c in range(1, 41):
            addr = _cell_addr(s_base, r, c)
            got = read_u16(cpu, addr)
            if r == 1 or r == 8:
                want = 0
            elif c == 1 or c == 40:
                want = 0
            else:
                want = 1
            _expect_eq(f"fill r{r} c{c}", got, want)


def _run_clear_test(cpu, mp_addr: int, s_base: int) -> None:
    _fill_array(cpu, s_base, 10, 42, 2)
    obstacles = [(1, 1), (4, 20), (8, 40)]
    _set_obstacles(cpu, s_base, obstacles)

    cpu.A.value = 1
    cpu.H.value = (mp_addr >> 8) & 0xFF
    cpu.L.value = mp_addr & 0xFF
    run_until_ret(cpu)

    for r in range(1, 9):
        for c in range(1, 41):
            addr = _cell_addr(s_base, r, c)
            got = read_u16(cpu, addr)
            want = 256 if (r, c) in obstacles else 2
            _expect_eq(f"clear r{r} c{c}", got, want)


def main() -> None:
    root = pathlib.Path(__file__).resolve().parents[2]
    default_asm = root / "assembly" / "17000_init_board.8085"
    default_sim = root / "tools" / "8085_harness" / "Sim8085"
    if not default_sim.exists():
        default_sim = root.parent / "Sim8085"

    parser = argparse.ArgumentParser(description="Project-specific 8085 tests for snowed_in.")
    parser.add_argument("--asm", type=pathlib.Path, default=default_asm, help="Path to .8085 source")
    parser.add_argument("--sim8085-path", type=pathlib.Path, default=default_sim, help="Path to Sim8085 repo")
    parser.add_argument("--mode", choices=["fill", "clear", "both"], default="both")
    args = parser.parse_args()

    asm, cpu_cls = assemble_source(args.asm, args.sim8085_path)
    cpu = load_program(asm, cpu_cls)

    mp_addr = 0x1000
    s_base = 0x2000
    _setup_mp(cpu, mp_addr, s_base)

    if args.mode in ("fill", "both"):
        _run_fill_test(cpu, mp_addr, s_base)

    if args.mode in ("clear", "both"):
        cpu = load_program(asm, cpu_cls)
        _setup_mp(cpu, mp_addr, s_base)
        _run_clear_test(cpu, mp_addr, s_base)

    print("OK")


if __name__ == "__main__":
    main()
