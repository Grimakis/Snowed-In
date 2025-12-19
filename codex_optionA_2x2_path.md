# Codex Instructions: Option A (No BFS) With a 2-Wide “Guaranteed Path” That Isn’t Boring
*(Model 100 BASIC, 8×40, walls-only obstacles; compatible with layered mini-templates + mirroring)*

Your current Option A works but feels boring because:
- rows 4–5 are always empty
- columns 1–3 and 38–40 are always empty

This update keeps the **no-validation guarantee** while allowing walls almost everywhere by protecting **only a 2-wide path** (a corridor that snakes), instead of protecting whole rows/columns.

---

## 1) New guarantee: a 2-wide protected path mask (P%)

### 1.1 What “2×2 width” means here
- The guaranteed path is always **2 tiles wide** (two stacked cells in every column).
- When the path “switches lanes” (between rows 3–4 and 4–5), we add a **turn pad** so the transition area includes a **2×2 open region** (actually a 3×1 column, which contains a 2×2 square with the next column).

This avoids the boring “entire rows are open”, while still guaranteeing a continuous left-to-right route.

### 1.2 Path states (very compact)
We define two corridor states:

- **State A:** path rows **3–4**
- **State B:** path rows **4–5**

Row **4** is always part of the path, so you can always spawn the player at `PR%=4`.

We store each path pattern as a list of **toggle columns** (columns where the path switches A↔B).

---

## 2) Data structures
Add a path mask array:

```basic
DIM P%(9,41)
```

Meaning:
- `P%(r,c)=1` => protected path cell (cannot place a wall here)
- `P%(r,c)=0` => can place a wall

---

## 3) Build the protected path (no expensive validation)

### 3.1 CLEAR_PATH
```basic
9000 REM CLEAR PATH MASK
9010 FOR R%=1 TO 8
9020 FOR C%=1 TO 40
9030 P%(R%,C%)=0
9040 NEXT C%
9050 NEXT R%
9060 RETURN
```

### 3.2 RESTORE toggle list for a path pattern (PATH%)
```basic
9100 REM RESTORE TOGGLES FOR PATH%
9110 IF PATH%=1 THEN RESTORE 16000
9120 IF PATH%=2 THEN RESTORE 16010
9130 IF PATH%=3 THEN RESTORE 16020
9140 IF PATH%=4 THEN RESTORE 16030
9150 IF PATH%=5 THEN RESTORE 16040
9160 RETURN
```

### 3.3 BUILD_PATH_2WIDE (PATH%)
This marks two path cells in every column, plus a “turn pad” at toggle columns.

```basic
9200 REM BUILD 2-WIDE PATH USING TOGGLE COLUMNS
9210 GOSUB 9000
9220 GOSUB 9100

9230 ST%=0       '0 = State A (rows 3-4), 1 = State B (rows 4-5)
9240 READ TG%    'next toggle column (or 0 to end)
9250 NEXTTG%=TG%

9260 FOR C%=1 TO 40
' mark corridor cells for this column
9270 IF ST%=0 THEN RT%=3 ELSE RT%=4
9280 P%(RT%,C%)=1
9290 P%(RT%+1,C%)=1

' if this column is a toggle, add a turn pad by also marking the other state in this column
9300 IF C%=NEXTTG% THEN
9310 IF ST%=0 THEN P%(5,C%)=1 ELSE P%(3,C%)=1
9320 ST%=1-ST%
9330 READ TG%:NEXTTG%=TG%
9340 END IF

9350 NEXT C%
9360 RETURN
```

---

## 4) Obstacles: change from “skip rows/cols” to “skip protected cells”
Replace your APPLY_LAYER filtering with:
- **only** skip walls where `P%(r,c)=1`

### 4.1 Update APPLY_LAYER (your 10380 block)
After decoding r,c and applying mirror/shift:

```basic
IF R%<2 OR R%>7 THEN 10420
IF C%<1 OR C%>40 THEN 10420
IF P%(R%,C%)<>0 THEN 10420
O%(R%,C%)=1
GOTO 10420
```

Remove these old constraints:
- `IF R%=4 OR R%=5 THEN ...`
- `IF C%<=3 OR C%>=38 THEN ...`

Now walls can appear in the middle and at start/end, but they can **never block** the protected path.

---

## 5) Generation flow (build path first, then obstacles)
In your obstacle builder (`10000`), do:

1) Clear obstacles
2) Pick a path pattern and build P%
3) Apply your layered templates, mirror/shift allowed

Pseudo-flow:

```basic
GOSUB 10240          'clear O%
PATH%=1+INT(RND(1)*5)
GOSUB 9200           'build P% protected path

GOSUB 10640          'apply layered templates (uses P% to skip)
```

### 5.1 Player start
Because row 4 is always protected, keep:
- `PR%=4 : PC%=1`

---

## 6) Drain windows (recommended, still cheap)
To avoid snow deadlocks, pick 2–3 “drain columns” where dumping to lawn remains possible by forbidding walls on row 2 and row 7 in those columns.

Add inside `9200` after the main loop (or during it):

```basic
P%(2,12)=1: P%(7,12)=1
P%(2,26)=1: P%(7,26)=1
P%(2,34)=1: P%(7,34)=1
```

---

## 7) Replacement mini-templates (more interesting, now safe via P%)
Keep your existing layer IDs and RESTORE mapping, but replace their DATA with these.

TOP 501–506:
```basic
14020 DATA 54,55,56,94,95,96,134,0
14060 DATA 70,71,72,73,110,111,112,0
14100 DATA 62,63,64,102,103,104,142,143,0
14140 DATA 49,89,129,169,209,0
14180 DATA 58,98,138,178,218,0
14220 DATA 66,67,68,106,107,108,146,147,148,0
```

BOTTOM 601–606:
```basic
14260 DATA 254,255,256,214,215,216,174,0
14300 DATA 270,271,272,273,230,231,232,0
14340 DATA 262,263,264,222,223,224,182,183,0
14380 DATA 289,249,209,169,129,0
14420 DATA 278,238,198,158,118,0
14460 DATA 266,267,268,226,227,228,186,187,188,0
```

SPICE 701–706 (small, stackable):
```basic
14500 DATA 60,100,220,260,0
14540 DATA 88,128,168,208,0
14580 DATA 112,152,192,232,0
14620 DATA 76,116,196,236,0
14660 DATA 96,136,216,256,0
14700 DATA 72,104,224,272,0
```

---

## 8) Path toggle DATA (PATH%=1..5)
Each list is columns where the path toggles; end with `0`.

```basic
16000 DATA 8,15,23,31,0
16010 DATA 6,12,18,27,35,0
16020 DATA 10,20,30,0
16030 DATA 5,9,14,22,28,33,0
16040 DATA 16,0
```

---

## 9) Summary: what Codex must change
1) Add `DIM P%(9,41)`
2) Add `9000`, `9100`, `9200` subs + toggle DATA
3) In obstacle build, call `BUILD_PATH_2WIDE` before applying layers
4) In APPLY_LAYER, remove “skip rows 4/5 and cols 1–3,38–40”; replace with `IF P%(R%,C%)<>0 THEN skip`
5) Replace old layer DATA with the new DATA
6) (Recommended) add drain windows via `P%` on rows 2 and 7

This keeps the program small, eliminates expensive validation, and makes maps visually and strategically more varied.
