# Codex Build Plan: Driveway Shoveler (Model 100 BASIC, 8x40)

## Goal
Build a playtestable TRS-80 Model 100 BASIC prototype with:
- Fixed board: 8 rows x 40 columns
- No obstacles for the initial playtest
- Snow as pushable boulders with counters
- Player never stands on snow
- No dumping off the house (left edge) or street (right edge)
- Only dumping into the lawn banks (top/bottom rows), which have a cap
- Win by clearing a continuous empty path of driveway cells from col 1 to col 40 through rows 2-7

## Board Model
**Dimensions**
- H = 8, W = 40

**Regions and caps**
- Rows 1 and 8 (lawn banks): unwalkable, snow depth 0-5 (cap 5)
- Rows 2-7 (driveway): walkable only if snow depth is 0, snow depth 0-3 (cap 3)

**Player state**
- Always: 2 <= PR <= 7, 1 <= PC <= 40, and S(PR,PC) = 0

## Initial State (no obstacles playtest)
- Leftmost driveway column cleared: for r=2..7, S(r,1) = 0
- Every other driveway tile starts at 1: for r=2..7, c=2..40, S(r,c) = 1
- Lawn rows start at 1: for r=1 and 8, c=1..40, S(r,c) = 1 (col 1 can be 0; no effect)
- Player start: PR=4, PC=1

## Controls
- Arrow keys if supported; otherwise W/A/S/D for up/left/down/right
- R restart
- Q quit

## Mechanics
1) **Movement (only onto empty driveway)**  
   If adjacent cell in direction dir is driveway with S=0, move there. Cannot move onto driveway snow (S>0) or lawn rows (1 or 8).

2) **Shoveling / pushing (1 unit per keypress)**  
   If adjacent cell SRC has S(SRC)>0, attempt to push 1 unit into DST (one step further in same dir). Push succeeds only if:
   - DST in bounds (no pushing off board edges)
   - S(DST) < cap(DST): cap 5 in rows 1 or 8; cap 3 in rows 2-7  
   On success: S(SRC) -= 1; S(DST) += 1; player does not move. On failure: no change.

3) **No dumping to house/street**  
   Any push where DST would be col 0, col 41, row 0, or row 9 is blocked.

## Win Condition
- A path of cleared driveway tiles exists from col 1 to col 40. Run BFS/flood fill on driveway cells with S=0 (rows 2-7). Start nodes: all (r,1) with S(r,1)=0. If any (r,40) is reachable, win.

## Rendering (8-line screen)
- Print exactly 8 rows each frame.
- Lawn rows (1 and 8): print digits 0-5 (single char).
- Driveway rows (2-7): `.` for 0; `1`..`3` for snow depth.
- Overlay player: print `P` at (PR,PC) (player cell must be 0).
- No extra HUD line initially. Optional: show `WIN` by temporarily replacing a row or printing once after win.

## Implementation Milestones
1. **Data + Draw**: DIM `S(8,40)` (or `S(9,41)` and ignore index 0). Implement `INIT` and `DRAW`.
2. **Input + Move**: Read a key; if target driveway cell has S=0, update (PR,PC).
3. **Push 1 unit**: If adjacent has snow, attempt shove into next cell with cap checks.
4. **Win Check**: BFS/flood fill after each action. On win, show message and wait for R or Q.
5. **Restart**: R calls `INIT` and redraws.

## Quick sanity tests
- From (4,1), pressing D repeatedly should first shovel the 1 at (4,2) into (4,3), then allow movement into (4,2) once it becomes 0, and quickly create jams like `...P13...` when compressing into cap-3.
