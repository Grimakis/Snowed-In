# Codex Doc: Implement Real Difficulty Levels (LV%=1..5) + Better RNG Seeding (Model 100 BASIC)
*(Driveway Shoveler / SNOW.DO, 8×40, whole-block pushing, layered obstacles + randomized snow)*

This document tells Codex exactly how to:
1) Make **LV% 1–5 actually differ** in difficulty (right now they all behave the same).
2) Improve **random seeding** so restarts within the same second don’t repeat layouts/snow.

This is designed to be lightweight and Model 100 BASIC-friendly (no heavy validation/BFS).

---

## A) Current behavior summary (baseline)
- `LV%=0` => no obstacles (`O%` cleared).
- `LV%=1..5` => **identical** generator today:
  - TOP layer (501–506) + BOTTOM layer (601–606) + 50% chance SPICE layer (701–706)
  - random mirror, occasional shift
- True “difficulty” today is mostly `SM%` (snow mode), not `LV%`.

Goal: make LV% control layout/obstacle complexity while SM% controls snow intensity.

---

## B) Proposed difficulty model (LV% 1–5)
Define these knobs (globals):
- `SPICEP!`   : probability of adding spice layer 1
- `SPICE2%`   : 0/1 add second spice layer (always distinct from spice1)
- `SHMODE%`   : shift mode (0 none, 1 small, 2 full)
- `DRAINS%`   : number of “drain window” columns to protect (reduces deadlocks)
- `DRPART%`   : 0 full drains only, 1 allow one “partial drain” (harder)
- `ZMIN%`     : minimum zero tiles required when RD%=1 snow is randomized (your 8460 check)
- `WALLCAP%`  : optional cap on total walls placed (reject extra layers if exceeded; cheap)

### Difficulty table
Use these defaults (tune later):
- **LV1 (Easy):**
  - `SPICEP!=0` , `SPICE2%=0`
  - `SHMODE%=0` (no shifts)
  - `DRAINS%=3` , `DRPART%=0`
  - `ZMIN%=14`
- **LV2:**
  - `SPICEP!=0.25`, `SPICE2%=0`
  - `SHMODE%=1` (small shifts only: -3,0,+3)
  - `DRAINS%=3` , `DRPART%=0`
  - `ZMIN%=12`
- **LV3 (Medium):**
  - `SPICEP!=0.50`, `SPICE2%=0`
  - `SHMODE%=1`
  - `DRAINS%=2` , `DRPART%=0`
  - `ZMIN%=10`
- **LV4 (Hard):**
  - `SPICEP!=0.75`, `SPICE2%=0`
  - `SHMODE%=2` (full shifts: -6,-3,0,+3,+6)
  - `DRAINS%=2` , `DRPART%=1` (one partial drain allowed)
  - `ZMIN%=8`
- **LV5 (Expert):**
  - `SPICEP!=1`, `SPICE2%=1`
  - `SHMODE%=2`
  - `DRAINS%=1` , `DRPART%=1`
  - `ZMIN%=6`

Notes:
- This keeps LV% meaningful even if SM% is OFF (deterministic snow).
- If SM% is HEAVY, LV4–5 should feel gnarly but not trivially unwinnable because drains still exist.

---

## C) Code changes for difficulty

### C1) Add SET_DIFF subroutine
Add a new routine (choose line range that fits) that sets all knobs based on `LV%`.

Example (pseudo; adjust line numbers):
```basic
12050 REM SET DIFFICULTY KNOBS FROM LV%
12060 SPICEP!=.5:SPICE2%=0:SHMODE%=1:DRAINS%=2:DRPART%=0:ZMIN%=10
12070 IF LV%=1 THEN SPICEP!=0:SPICE2%=0:SHMODE%=0:DRAINS%=3:DRPART%=0:ZMIN%=14
12080 IF LV%=2 THEN SPICEP!=.25:SPICE2%=0:SHMODE%=1:DRAINS%=3:DRPART%=0:ZMIN%=12
12090 IF LV%=3 THEN SPICEP!=.5:SPICE2%=0:SHMODE%=1:DRAINS%=2:DRPART%=0:ZMIN%=10
12100 IF LV%=4 THEN SPICEP!=.75:SPICE2%=0:SHMODE%=2:DRAINS%=2:DRPART%=1:ZMIN%=8
12110 IF LV%=5 THEN SPICEP!=1:SPICE2%=1:SHMODE%=2:DRAINS%=1:DRPART%=1:ZMIN%=6
12120 RETURN
```

### C2) Call SET_DIFF at start of a run
Call `GOSUB SET_DIFF` in two places:
- right after level selection returns
- and also on restart if LV% can change

In your current flow, a good place is after `GOSUB 7000` (level menu) and before `GOSUB 10000`:
```basic
GOSUB 7000
GOSUB 12050
GOSUB 10000
```

### C3) Use ZMIN% in your snow validation
Right now `8460` hardcodes `Z%<10`. Replace with `Z%<ZMIN%`.

```basic
8600 OK%=1:IF Z%<ZMIN% THEN OK%=0
```

### C4) Modify BUILD RANDOM LAYOUT to respect difficulty knobs
In `10640`, instead of fixed “50% spice”, do:

- Always apply TOP + BOTTOM.
- Add SPICE layer 1 if `RND(1) < SPICEP!`.
- Add SPICE layer 2 if `SPICE2%<>0` (choose distinct spice ID).

Also: implement `SHMODE%`:
- `SHMODE%=0`: `SH%=0`
- `SHMODE%=1`: shifts from `{-3,0,+3}`
- `SHMODE%=2`: shifts from `{-6,-3,0,+3,+6}`

Provide two small helper subs (or inline code).

Pseudo edits inside `10640`:

```basic
'TOP
LI%=501+INT(RND(1)*6)
MI%=INT(RND(1)*2)
GOSUB 12200  'PICK_SHIFT -> sets SH%
GOSUB 10380

'BOTTOM
LI%=601+INT(RND(1)*6)
MI%=INT(RND(1)*2)
GOSUB 12200
GOSUB 10380

'SPICE1
IF RND(1) >= SPICEP! THEN 10940
LI%=701+INT(RND(1)*6)
MI%=INT(RND(1)*2)
GOSUB 12200
GOSUB 10380

'SPICE2 (distinct)
IF SPICE2%=0 THEN 10940
LI2%=701+INT(RND(1)*6)
IF LI2%=LI% THEN LI2%=701+((LI2%-701+1) MOD 6)
LI%=LI2%
MI%=INT(RND(1)*2)
GOSUB 12200
GOSUB 10380
```

### C5) Add PICK_SHIFT helper
```basic
12200 REM PICK_SHIFT INTO SH% FROM SHMODE%
12210 SH%=0
12220 IF SHMODE%=0 THEN RETURN
12230 IF SHMODE%=1 THEN SH%=-3+3*INT(RND(1)*3):RETURN   ' -3,0,+3
12240 IF SHMODE%=2 THEN SH%=-6+3*INT(RND(1)*5):RETURN   ' -6,-3,0,+3,+6
12250 RETURN
```

---

## D) Drain windows (difficulty-controlled, cheap)
Drain windows reduce deadlocks by ensuring some columns can always dump snow to the lawn (row 1 / row 8).

Implementation approach depends on whether you’re using the “P% path mask” system. If you are:
- Mark drains as protected in `P%` on row 2 and row 7.

If you are not using P%, you can do it in APPLY_LAYER by skipping walls when `(R%=2 OR R%=7)` in a drain column.

### D1) Choose drain columns from small presets
To keep code small, define 3 drain sets (columns chosen to be well-spaced):
- Set A: 12, 26, 34
- Set B: 10, 22, 36
- Set C: 14, 28, 32

Pick one set randomly each level build.

### D2) Apply drains based on DRAINS% and DRPART%
Rules:
- If `DRAINS%=3`: protect all 3 columns (full drains)
- If `DRAINS%=2`: protect first 2 columns
- If `DRAINS%=1`: protect only the first column
- If `DRPART%=1`: allow the last drain to be partial:
  - protect only row 2 OR only row 7 (randomly)

### D3) Suggested implementation if using P%
Add a `SET_DRAINS` subroutine called during obstacle build before applying layers:

```basic
12300 REM SET DRAINS USING P% MASK
12310 DS%=1+INT(RND(1)*3)   '1=A,2=B,3=C
12320 IF DS%=1 THEN D1%=12:D2%=26:D3%=34
12330 IF DS%=2 THEN D1%=10:D2%=22:D3%=36
12340 IF DS%=3 THEN D1%=14:D2%=28:D3%=32

12350 GOSUB 12400  'apply D1 as full drain
12360 IF DRAINS%>=2 THEN GOSUB 12420
12370 IF DRAINS%>=3 THEN GOSUB 12440
12380 RETURN

12400 REM APPLY FULL DRAIN COL D1%
12410 P%(2,D1%)=1:P%(7,D1%)=1:RETURN

12420 REM APPLY FULL DRAIN COL D2%
12430 P%(2,D2%)=1:P%(7,D2%)=1:RETURN

12440 REM APPLY D3 (FULL OR PARTIAL)
12450 IF DRPART%=0 THEN P%(2,D3%)=1:P%(7,D3%)=1:RETURN
12460 IF RND(1)<.5 THEN P%(2,D3%)=1 ELSE P%(7,D3%)=1
12470 RETURN
```

If you aren’t using P%, replace `P%` assignments with logic in APPLY_LAYER:
- if R in {2,7} and C is a drain col => skip placement.

---

## E) Better RNG seeding (fix repeats within the same second)

### E1) Problem with current seed
Your current seeding uses `RIGHT$(TIME$,2)` (seconds). If you restart quickly, it repeats.

### E2) Better seed strategy (still BASIC-friendly)
We want entropy from:
- seconds, minutes, hours (TIME$)
- number of keypresses / loop count since program start
- a rolling “noise” variable updated continuously

Implement two globals:
- `NOISE%` increments in the input loop
- `SEED%` derived from TIME$ + NOISE%

### E3) Add a rolling NOISE% update
In the main input loop, increment NOISE% even when no key is pressed:

Example near your `K$=INKEY$` loop:
```basic
NOISE%=NOISE%+1:IF NOISE%>30000 THEN NOISE%=0
```

### E4) New SEED_RNG routine
Replace your `8000` with a stronger seed that uses HH:MM:SS and NOISE%.

Model 100 TIME$ is typically "HH:MM:SS". Use MID$:

```basic
8000 REM SEED RNG (BETTER)
8010 H%=VAL(LEFT$(TIME$,2))
8020 M%=VAL(MID$(TIME$,4,2))
8030 S%=VAL(RIGHT$(TIME$,2))
8040 SEED%=H%*3600+M%*60+S%+NOISE%
8050 IF SEED%<1 THEN SEED%=1
8060 FOR I%=1 TO (SEED% MOD 97)+10
8070 U!=RND(1)
8080 NEXT I%
8090 RETURN
```

Notes:
- The `(SEED% MOD 97)+10` loop is short but varied enough to scramble RND’s state.
- NOISE% ensures quick restarts still change the scramble count.

### E5) Where to call SEED_RNG
- Call it once before obstacle generation
- Call it again (optional) before snow randomization if you want independent streams
- Do not call it repeatedly every frame; that can reduce randomness

---

## F) Minimal integration checklist for Codex
1) Add globals: `SPICEP!`, `SPICE2%`, `SHMODE%`, `DRAINS%`, `DRPART%`, `ZMIN%`, `NOISE%`
2) Implement `SET_DIFF` and call it after level menu
3) Replace `8460` threshold with `ZMIN%`
4) Update layout builder `10640` to use `SPICEP!`, `SPICE2%`, and `PICK_SHIFT`
5) Add drain window logic (P% mask or APPLY_LAYER rule)
6) Replace `8000` seeding with the improved TIME$+NOISE% version
7) Add `NOISE%` increments in the main loop

This yields:
- LV% 1–5 feel different
- restarts don’t repeat nearly as often
- still no heavy validation required
