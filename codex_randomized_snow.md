# Codex Instructions: Randomized Starting Snow (Model 100 BASIC, 8×40)

Implement a feature to **randomize the starting snow depth** on the driveway using **controlled ratios**:
- some tiles start at **0** (cleared)
- some tiles start at **2**
- remaining tiles start at **1**

The ratios are controlled by **floating-point variables**.

This is for an **8 rows × 40 columns** grid, where:
- driveway rows are **2–7**
- lawn/bank rows are **1 and 8** (can remain fixed or be handled separately)
- player cannot stand on snow (player cell must be 0)
- walls (if present) should always have snow = 0

---

## 1) Inputs / Configuration

Add these floating-point variables (single precision is fine):

- `P0!` = probability a driveway tile starts at **0**
- `P2!` = probability a driveway tile starts at **2**
- `P1!` is implied: `P1! = 1 - P0! - P2!` (probability of **1**)

**Constraints:**
- `0 <= P0! <= 1`
- `0 <= P2! <= 1`
- `P0! + P2! <= 1`

Recommended defaults for early playtests:
- `P0! = 0.15` (15% zeros)
- `P2! = 0.10` (10% twos)
- rest are ones

---

## 2) Where this runs in your program

Call this after:
1) walls/templates are loaded into `O%(r,c)` (if you have obstacles)
2) you are initializing the snow array `S%(r,c)`

Suggested order inside your init routine:

1. Clear/reset `S%`
2. Fill banks (row 1 and 8) however you want (fixed is fine for now)
3. Randomize driveway rows 2–7 using `P0!`, `P2!`
4. Enforce invariants (spawn strip, goal column, walls, player tile)

---

## 3) Invariants to enforce (important)

After randomization, enforce these rules:

### Spawn strip clear
- Clear the leftmost driveway column so the player always has a start area:
  - For `r = 2..7`: `S%(r,1) = 0`

### Player cell clear
- Ensure the player’s start cell is 0:
  - `PR%=4: PC%=1`
  - `S%(PR%,PC%)=0`

### Goal column (if you keep “reach col 40”)
If your rules disallow dumping off the right edge, it is usually necessary to keep column 40 enterable:
- simplest: clear the goal column on the driveway:
  - for `r=2..7`: `S%(r,40)=0`
OR
- if you treat col 40 as boundary and goal is col 39, skip this.

### Walls override snow (if using O%)
- if `O%(r,c) <> 0` then `S%(r,c)=0` (no snow inside walls)

---

## 4) Random assignment rule (core algorithm)

For each driveway tile `(r,c)` in rows 2–7 and columns 2–39 (or 2–40 if you want), do:

1) generate `U! = RND(1)` which returns a float in `[0,1)`
2) if `U! < P0!` then assign `S%=0`
3) else if `U! < P0! + P2!` then assign `S%=2`
4) else assign `S%=1`

That’s it.

---

## 5) Model 100 BASIC implementation sketch

### A) Add parameters (somewhere near the top / init)
```basic
P0!=0.15
P2!=0.10
```

### B) Randomize seed (optional but recommended)
If you want different boards each run:
- `RANDOMIZE TIMER` (if supported)
or
- `RANDOMIZE VAL(RIGHT$(TIME$,2))` style (depending on available functions)

Example:
```basic
RANDOMIZE TIMER
```

### C) Subroutine: Randomize driveway snow
Create a new subroutine (example at line 5200):

```basic
5200 REM RANDOMIZE DRIVEWAY SNOW USING P0!, P2!
5210 FOR R%=2 TO 7
5220 FOR C%=2 TO 39
5230 IF O%(R%,C%)<>0 THEN S%(R%,C%)=0:GOTO 5260
5240 U!=RND(1)
5250 IF U!<P0! THEN S%(R%,C%)=0 ELSE IF U!<P0!+P2! THEN S%(R%,C%)=2 ELSE S%(R%,C%)=1
5260 NEXT C%
5270 NEXT R%
5280 RETURN
```

Notes:
- The `O%` check is optional if you don’t have walls yet.
- Columns `2..39` avoids stomping your spawn strip at col 1 and keeps col 40 free for your win condition if you want.
- If you want randomization to include col 40, change the loop to `C%=2 TO 40`, but then you must re-clear goal tiles afterwards if needed.

### D) Enforce invariants after randomization
After calling the randomizer sub, do:

```basic
FOR R%=2 TO 7: S%(R%,1)=0: NEXT R%
FOR R%=2 TO 7: S%(R%,40)=0: NEXT R%  'only if goal is col 40 and you need it enterable
S%(PR%,PC%)=0
```

---

## 6) Optional: Guardrails to avoid “bad” random boards (recommended)

Random boards can sometimes be unfun (too many 2s clustered, too few zeros, etc).
Add a cheap “quality” check and reroll.

### Example guardrails
After randomization, count:
- `Z%` = number of driveway tiles with 0 in rows 2–7, cols 2–39
- `T%` = number of driveway tiles with 2 in rows 2–7, cols 2–39

Require:
- `Z% >= 10` (at least some workspace)
- `T% <= 25` (avoid too many heavy piles early)

If failed: reroll up to N times (e.g. 5).

Sketch:

```basic
5300 REM VALIDATE RANDOM SNOW (RETURNS OK% = 1/0)
5310 Z%=0:T%=0
5320 FOR R%=2 TO 7
5330 FOR C%=2 TO 39
5340 IF S%(R%,C%)=0 THEN Z%=Z%+1
5350 IF S%(R%,C%)=2 THEN T%=T%+1
5360 NEXT C%
5370 NEXT R%
5380 OK%=1
5390 IF Z%<10 THEN OK%=0
5400 IF T%>25 THEN OK%=0
5410 RETURN
```

Then in init:

```basic
TRIES%=0
DO
  GOSUB 5200
  GOSUB 5300
  TRIES%=TRIES%+1
LOOP WHILE OK%=0 AND TRIES%<5
```

If your BASIC doesn’t support `DO/LOOP`, use `GOTO`.

---

## 7) Testing checklist
1) With `P0!=0` and `P2!=0`, you see a mix of 0/1/2 on driveway.
2) Spawn strip (col 1) on rows 2–7 is always clear.
3) Player starts on a clear cell.
4) If using goal col 40, at least one cell in col 40 is clear (or you clear it).
5) Walls (if any) always show as walls and have no snow values.

---

## 8) Quick tuning suggestions
- Too easy: decrease `P0!`, increase `P2!`
- Too jammy: increase `P0!`, decrease `P2!`
- If you later add level difficulty, make `P0!`/`P2!` depend on `LEVEL%`.

