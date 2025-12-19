# Codex Instructions: Option A Layered Maps (Guaranteed Winnable) + Replacement Mini-Templates
*(TRS-80 Model 100 BASIC, 8×40, walls-only)*

This implements **Option A**: generate many layouts by combining small wall “layers”, while guaranteeing the map is *geometrically winnable* **without doing expensive validation**.

The guarantee comes from a **protected corridor**: walls are never allowed on rows **4–5**, so there is always an open left-to-right route (ignoring snow).

You will also replace the previous mini-templates with a safer library that:
- avoids protected columns
- is designed to be additive (multiple layers combine without bricking)
- still affects gameplay by blocking vertical dumping above/below the corridor

---

## 1) Option A guarantee (no BFS needed)

### 1.1 Protected corridor
**Never place walls in driveway rows 4 and 5.**

- Driveway rows are 2..7
- Corridor rows are **4 and 5**
- Therefore, the open cells on rows 4–5 form an always-available path across the map.

### 1.2 Protected zones (recommended)
To keep playability high and avoid accidental “hard starts/finishes”:

- **Spawn zone columns:** 1–3 (driveway rows)
- **Finish zone columns:** 38–40 (driveway rows)

**Never place walls in these columns.**

Result: even when layers combine, you still have room to maneuver at start/end.

---

## 2) Data structures

Keep / add:
- `DIM O%(9,41)` walls (0 empty, 1 wall)
- `DIM S%(9,41)` snow
- `SEED%` optional if you randomize layer selection
- `MODE%` optional if you choose between “Realistic” and “Abstract”

---

## 3) Layer storage format (compact)

Store each layer as a list of linear indices terminated with `0`:

- `IDX = (r-1)*40 + c`  where `r=1..8`, `c=1..40`
- Only rows 2..7 are meaningful for walls; we also **filter** in code.

Example: wall at (r=3,c=10) => `IDX=90`.

---

## 4) Applying layers (with mirror + shift + corridor rules)

### 4.1 Apply-layer rules
When applying a wall cell (r,c) from a layer (after mirror/shift):
- Skip if `r` is not in driveway: `r<2 OR r>7`
- Skip if `r` is corridor: `r=4 OR r=5`
- Skip if `c` is protected zone: `c<=3 OR c>=38`
- Skip if out of bounds: `c<1 OR c>40`
- Otherwise set: `O%(r,c)=1`

### 4.2 Mirror and shift
- `MIRROR%` = 0/1; if 1 then `c = 41 - c`
- `SHIFT%` can be from set `{ -6, -3, 0, +3, +6 }`
- After shift: `c = c + SHIFT%`

Because we filter protected columns + corridor rows, even “bad” transformations become safe.

---

## 5) Code blocks to add

### 5.1 CLEAR_OBS
```basic
8100 REM CLEAR OBSTACLES
8110 FOR R%=1 TO 8
8120 FOR C%=1 TO 40
8130 O%(R%,C%)=0
8140 NEXT C%
8150 NEXT R%
8160 RETURN
```

### 5.2 RESTORE dispatcher (Layer ID -> DATA)
Implement this mapping using IF statements. The IDs below match the DATA blocks in Section 8.

```basic
8400 REM RESTORE LAYER BY ID (LID%)
8410 IF LID%=501 THEN RESTORE 9500
8420 IF LID%=502 THEN RESTORE 9520
8430 IF LID%=503 THEN RESTORE 9540
8440 IF LID%=504 THEN RESTORE 9560
8450 IF LID%=505 THEN RESTORE 9580
8460 IF LID%=506 THEN RESTORE 9600

8470 IF LID%=601 THEN RESTORE 9620
8480 IF LID%=602 THEN RESTORE 9640
8490 IF LID%=603 THEN RESTORE 9660
8500 IF LID%=604 THEN RESTORE 9680
8510 IF LID%=605 THEN RESTORE 9700
8520 IF LID%=606 THEN RESTORE 9720

8530 IF LID%=701 THEN RESTORE 9740
8540 IF LID%=702 THEN RESTORE 9760
8550 IF LID%=703 THEN RESTORE 9780
8560 IF LID%=704 THEN RESTORE 9800
8570 IF LID%=705 THEN RESTORE 9820
8580 IF LID%=706 THEN RESTORE 9840
8590 RETURN
```

### 5.3 APPLY_LAYER (uses corridor + protected zones)
Use safe integer mapping for Model 100 BASIC:

```basic
8200 REM APPLY LAYER LID% WITH MIRROR% SHIFT%
8210 GOSUB 8400
8220 READ IDX%
8230 IF IDX%=0 THEN RETURN
8240 R%=INT((IDX%-1)/40)+1
8250 C%=IDX%-(R%-1)*40
8260 IF MIRROR%<>0 THEN C%=41-C%
8270 C%=C%+SHIFT%
8280 IF R%<2 OR R%>7 THEN 8220
8290 IF R%=4 OR R%=5 THEN 8220
8300 IF C%<1 OR C%>40 THEN 8220
8310 IF C%<=3 OR C%>=38 THEN 8220
8320 O%(R%,C%)=1
8330 GOTO 8220
```

### 5.4 BUILD_RANDOM_LAYOUT (Option A)
Recipe: 1 TOP + 1 BOTTOM + optional SPICE.

- TOP layers: 501–506
- BOTTOM layers: 601–606
- SPICE layers: 701–706

```basic
8600 REM BUILD RANDOM LAYOUT (OPTION A)
8610 GOSUB 8100

'Pick TOP
8620 LID%=501+INT(RND(1)*6)
8630 MIRROR%=INT(RND(1)*2)
8640 SHIFT%=0:IF RND(1)<.5 THEN SHIFT%=(-6)+3*INT(RND(1)*5)  ' -6,-3,0,3,6
8650 GOSUB 8200

'Pick BOTTOM
8660 LID%=601+INT(RND(1)*6)
8670 MIRROR%=INT(RND(1)*2)
8680 SHIFT%=0:IF RND(1)<.5 THEN SHIFT%=(-6)+3*INT(RND(1)*5)
8690 GOSUB 8200

'Optional SPICE (50%)
8700 IF RND(1)<.5 THEN 8740
8710 LID%=701+INT(RND(1)*6)
8720 MIRROR%=INT(RND(1)*2)
8730 SHIFT%=0:IF RND(1)<.5 THEN SHIFT%=(-6)+3*INT(RND(1)*5)
8735 GOSUB 8200
8740 RETURN
```

**Note:** If you want “Realistic vs Abstract”, keep Option A guarantee the same, but maintain two pools and choose which pool to draw from. The templates below are tuned to be corridor-safe.

---

## 6) Integrate with your current init flow

At game start (after title/menu) and on restart:
1) Build layout: `GOSUB 8600` (or a fixed recipe per Level)
2) Init snow: `GOSUB 500` (your init)
3) Force `S%` under walls to 0 (you already do this)
4) Draw

---

## 7) Why these templates are “safe”
- They **never place walls on rows 4–5**, so connectivity exists by design.
- They mostly place walls on rows 2–3 and 6–7, which:
  - blocks vertical dumping above/below corridor in some columns
  - creates “no-dump columns” without sealing the map
- They avoid columns 1–3 and 38–40 by construction (and the apply filter enforces it anyway).

---

## 8) Replacement mini-template DATA blocks (paste into program)

Legend:
- TOP band (rows 2–3): IDs **501–506**
- BOTTOM band (rows 6–7): IDs **601–606**
- SPICE (small mixed): IDs **701–706**

All lists are compact IDX values terminated with `0`.

```basic
9499 REM LAYER 501 TOP1_PORCH_POSTS
9500 DATA 55,65,90,100,110,0

9519 REM LAYER 502 TOP2_BROKEN_BAR
9520 DATA 92,93,94,95,96,102,103,104,105,106,0

9539 REM LAYER 503 TOP3_STAIR
9540 DATA 52,54,56,65,93,95,97,104,106,0

9559 REM LAYER 504 TOP4_THREE_PILLAR_PAIRS
9560 DATA 54,62,68,94,102,108,0

9579 REM LAYER 505 TOP5_TWIN_2X2S
9580 DATA 51,52,67,68,91,92,107,108,0

9599 REM LAYER 506 TOP6_SPARSE_LINE
9600 DATA 49,57,65,73,93,101,109,0


9619 REM LAYER 601 BOT1_PORCH_POSTS
9620 DATA 210,220,230,255,265,0

9639 REM LAYER 602 BOT2_BROKEN_BAR
9640 DATA 212,213,214,215,216,222,223,224,225,226,0

9659 REM LAYER 603 BOT3_STAIR
9660 DATA 213,215,217,224,226,252,254,256,265,0

9679 REM LAYER 604 BOT4_THREE_PILLAR_PAIRS
9680 DATA 214,222,228,254,262,268,0

9699 REM LAYER 605 BOT5_TWIN_2X2S
9700 DATA 211,212,227,228,251,252,267,268,0

9719 REM LAYER 606 BOT6_SPARSE_LINE
9720 DATA 213,221,229,249,257,265,273,0


9739 REM LAYER 701 SP1_CENTER_DUMP_BLOCKERS
9740 DATA 60,98,103,218,223,260,0

9759 REM LAYER 702 SP2_LEFT_MID
9760 DATA 50,88,208,250,0

9779 REM LAYER 703 SP3_RIGHT_MID
9780 DATA 70,112,232,270,0

9799 REM LAYER 704 SP4_DIAG_SPRINKLE
9800 DATA 52,68,95,226,254,269,0

9819 REM LAYER 705 SP5_TWIN_PAIRS
9820 DATA 56,96,224,264,0

9839 REM LAYER 706 SP6_SCATTER6
9840 DATA 62,106,214,230,258,274,0
```

---

## 9) Quick manual sanity test (expected behavior)
After `BUILD_RANDOM_LAYOUT`, visually inspect:
- Rows 4 and 5 contain **no `#`**
- Columns 1–3 and 38–40 contain **no `#`**
- Most walls appear in rows 2–3 and 6–7
- Player can always walk across via row 4/5 once snow is cleared there

---

## 10) Optional: Make it feel less “always corridor”
If the corridor feels too samey, keep it open but encourage detours:
- Bias starting snow so corridor rows tend to be heavier (more 2s), while top/bottom rows have more 0s.
- This keeps winnability but makes leaving the corridor attractive.

