# Codex Instructions: Layered Wall Templates + Mirroring (Model 100 BASIC, 8×40)

This document describes a **mix-and-match level system** built from small **wall layers** that can be combined to generate many layouts.

You will:
- Store each layer as a compact **index list** (`IDX = (r-1)*40 + c`, 1..320)
- Combine layers by OR-ing walls into `O%(r,c)`
- Optionally **mirror horizontally** and **shift** each layer before applying
- Validate the combined layout to avoid impossible runs

---

## 1) Data structures

Add/keep these globals:
- `DIM O%(9,41)`  obstacle grid (0 empty, 1 wall)
- `DIM S%(9,41)`  snow grid
- `LEVEL%` optional (if you still have fixed levels)
- `SEED%` optional (if you randomize layer choices)

Recommended: apply walls only on driveway rows 2..7.


## 2) Core subroutines

### 2.1 CLEAR_OBS (clears O%)
```basic
8100 REM CLEAR OBSTACLES
8110 FOR R%=1 TO 8
8120 FOR C%=1 TO 40
8130 O%(R%,C%)=0
8140 NEXT C%
8150 NEXT R%
8160 RETURN
```

### 2.2 APPLY_LAYER(LID%, MIRROR%, SHIFT%)
Reads an index list for a layer and writes walls into `O%`.

- `MIRROR%`: 0=no mirror, 1=mirror horizontally (c -> 41-c)
- `SHIFT%`: integer column shift (e.g., -8,-4,0,+4,+8). If shifted out of bounds, skip that wall.

```basic
8200 REM APPLY LAYER LID% WITH OPTIONAL MIRROR/SHIFT
8210 GOSUB 8400  'RESTORE to the correct DATA block for LID%
8220 READ IDX%
8230 IF IDX%=0 THEN RETURN
8240 R%=INT((IDX%-1)/40)+1
8250 C%=IDX%-(R%-1)*40
8260 IF MIRROR%<>0 THEN C%=41-C%
8270 C%=C%+SHIFT%
8280 IF R%<2 OR R%>7 OR C%<1 OR C%>40 THEN 8220
8290 O%(R%,C%)=1
8300 GOTO 8220
```

### 2.3 RESTORE_TABLE (maps LID% -> RESTORE line)
Implement as IF/THEN chain (fast enough at this scale).

```basic
8400 REM RESTORE DATA FOR LAYER ID LID%
8410 IF LID%=101 THEN RESTORE 9100
8420 IF LID%=102 THEN RESTORE 9120
8430 IF LID%=103 THEN RESTORE 9140
8440 IF LID%=104 THEN RESTORE 9160
8450 IF LID%=105 THEN RESTORE 9180
8460 IF LID%=106 THEN RESTORE 9200

8470 IF LID%=201 THEN RESTORE 9300
8480 IF LID%=202 THEN RESTORE 9320
8490 IF LID%=203 THEN RESTORE 9340
8500 IF LID%=204 THEN RESTORE 9360
8510 IF LID%=205 THEN RESTORE 9380
8520 IF LID%=206 THEN RESTORE 9400

8530 IF LID%=301 THEN RESTORE 9500
8540 IF LID%=302 THEN RESTORE 9520
8550 IF LID%=303 THEN RESTORE 9540
8560 IF LID%=304 THEN RESTORE 9560
8570 IF LID%=305 THEN RESTORE 9580
8580 IF LID%=306 THEN RESTORE 9600

8590 IF LID%=401 THEN RESTORE 9700
8600 IF LID%=402 THEN RESTORE 9720
8610 IF LID%=403 THEN RESTORE 9740
8620 IF LID%=404 THEN RESTORE 9760
8630 IF LID%=405 THEN RESTORE 9780
8640 IF LID%=406 THEN RESTORE 9800
8650 RETURN
```


## 3) Building a level from layers

Use a simple recipe:

- Choose **one Structure** (either Realistic *or* Abstract)
- Choose **0–1 Fence**
- Choose **1–2 Post clusters** (distinct)

Then:
1) `GOSUB 8100` (CLEAR_OBS)
2) Apply each chosen layer with its own mirror/shift parameters
3) Validate
4) Continue into your normal snow init

Example (hand-chosen):
```basic
'Structure: Realistic Car (101), mirrored, shift +4
L1%=101: M1%=1: SH1%=4
'Fence: none (0)
L2%=0
'Posts: scatter (402), no mirror, shift 0
L3%=402: M3%=0: SH3%=0
'Posts: right bay (405), mirror, shift -4
L4%=405: M4%=1: SH4%=-4

GOSUB 8100
GOSUB 8200  'apply layer 1 (set LID% etc before call)
```

Implementation note: in BASIC, set globals before calling APPLY_LAYER:
- `LID%=... : MIRROR%=... : SHIFT%=... : GOSUB 8200`


## 4) Validation (prevents impossible mixes)

After combining layers, run quick checks. If invalid, reroll your layer choices.

### 4.1 No fully-blocked columns (rows 2..7)
```basic
8700 REM VALIDATE: NO SOLID WALL COLUMNS ACROSS DRIVEWAY
8710 FOR C%=1 TO 40
8720 OPEN%=0
8730 FOR R%=2 TO 7
8740 IF O%(R%,C%)=0 THEN OPEN%=1
8750 NEXT R%
8760 IF OPEN%=0 THEN OK%=0:RETURN
8770 NEXT C%
8780 OK%=1:RETURN
```

Also recommended:
- Ensure at least one open cell exists in goal column (40 or 39, depending on your win rule)
- Ensure spawn strip (col 1 rows 2..7) is not walled


## 5) Layer library

Each layer is a compact DATA list of indices terminated with `0`.


### 5.1 Realistic Structures (IDs 101–106)

- **101 RS1_CAR_3x6**: big parked car rectangle (solid)
- **102 RS2_TWO_BLOCKS**: two small obstacles (like snowman/sled clusters)
- **103 RS3_L_SHAPE**: L-shaped bump-out near the left
- **104 RS4_THREE_SHRUBS**: three small shrub rectangles
- **105 RS5_DIAG_CAR**: diagonal-ish “car” (staircase thickness 2)
- **106 RS6_ISLAND_4x4**: solid 4×4 island


### 5.2 Abstract Structures (IDs 201–206)

- **201 AS1_TWIN_PILLARS**: two columns with staggered gaps
- **202 AS2_ZIGZAG**: single-tile zigzag diagonal
- **203 AS3_FENCE_ROW5_GAP2**: long horizontal fence with a 2-tile gap
- **204 AS4_HOLLOW_BOX**: hollow rectangle outline (thicker puzzle feel)
- **205 AS5_TWO_BARS**: two horizontal bars with offset gaps
- **206 AS6_CHECKER_CLUSTER**: checkerboard cluster region


### 5.3 Fence Layers (IDs 301–306)

- **301 F1_VERT_FENCE_GAP2**: short vertical fence with 2-row gap
- **302 F2_HORZ_FENCE_GAP1**: short horizontal fence with 1 gap
- **303 F3_CORNER**: corner fence near right
- **304 F4_SPARSE_PILLARS**: sparse pillars
- **305 F5_BAR**: short horizontal bar
- **306 F6_DIAG**: diagonal fence


### 5.4 Post Clusters (IDs 401–406)

- **401 P1_FOUR_POSTS**
- **402 P2_SCATTER6**
- **403 P3_NEAR_CENTER5**
- **404 P4_LEFT_BAY4**
- **405 P5_RIGHT_BAY4**
- **406 P6_TOP_BOTTOM_PAIR6**


---
## 6) DATA blocks (paste into your program)

These lines define the layer library. They assume the RESTORE mapping in `8400`.

```basic

9099 REM LAYER 101 RS1_CAR_3x6
9100 DATA 140,141,142,143,144,145,180,181,182,183,184,185
9101 DATA 220,221,222,223,224,225,0

9119 REM LAYER 102 RS2_TWO_BLOCKS
9120 DATA 94,95,134,135,230,231,270,271,0

9139 REM LAYER 103 RS3_L_SHAPE
9140 DATA 48,49,50,88,128,168,169,170,171,172,0

9159 REM LAYER 104 RS4_THREE_SHRUBS
9160 DATA 62,63,64,102,103,104,153,154,155,170,171,172
9161 DATA 193,194,195,210,211,212,0

9179 REM LAYER 105 RS5_DIAG_CAR
9180 DATA 58,59,99,100,140,141,181,182,222,223,263,264
9181 DATA 0

9199 REM LAYER 106 RS6_ISLAND_4x4
9200 DATA 106,107,108,109,146,147,148,149,186,187,188,189
9201 DATA 226,227,228,229,0

9299 REM LAYER 201 AS1_TWIN_PILLARS
9300 DATA 58,63,98,103,143,178,218,223,258,263,0

9319 REM LAYER 202 AS2_ZIGZAG
9320 DATA 68,107,146,185,224,263,0

9339 REM LAYER 203 AS3_FENCE_ROW5_GAP2
9340 DATA 172,173,174,175,176,177,178,179,182,183,184,185
9341 DATA 186,187,188,189,0

9359 REM LAYER 204 AS4_HOLLOW_BOX
9360 DATA 96,97,98,99,100,101,102,103,104,136,144,176
9361 DATA 184,216,217,218,219,220,221,222,223,224,0

9379 REM LAYER 205 AS5_TWO_BARS
9380 DATA 88,89,90,91,92,95,96,97,98,99,100,220
9381 DATA 221,222,223,224,225,226,229,230,231,232,0

9399 REM LAYER 206 AS6_CHECKER_CLUSTER
9400 DATA 132,134,136,138,173,175,177,179,212,214,216,218
9401 DATA 0

9499 REM LAYER 301 F1_VERT_FENCE_GAP2
9500 DATA 70,110,230,270,0

9519 REM LAYER 302 F2_HORZ_FENCE_GAP1
9520 DATA 126,127,128,129,131,132,133,134,135,136,0

9539 REM LAYER 303 F3_CORNER
9540 DATA 70,71,72,73,74,75,115,155,195,0

9559 REM LAYER 304 F4_SPARSE_PILLARS
9560 DATA 52,69,92,189,212,269,0

9579 REM LAYER 305 F5_BAR
9580 DATA 165,166,167,168,169,170,171,172,173,174,175,0

9599 REM LAYER 306 F6_DIAG
9600 DATA 72,111,150,189,228,267,0

9699 REM LAYER 401 P1_FOUR_POSTS
9700 DATA 90,142,217,273,0

9719 REM LAYER 402 P2_SCATTER6
9720 DATA 65,109,134,168,236,259,0

9739 REM LAYER 403 P3_NEAR_CENTER5
9740 DATA 99,140,144,181,222,0

9759 REM LAYER 404 P4_LEFT_BAY4
9760 DATA 46,87,207,246,0

9779 REM LAYER 405 P5_RIGHT_BAY4
9780 DATA 74,115,235,274,0

9799 REM LAYER 406 P6_TOP_BOTTOM_PAIR6
9800 DATA 56,64,108,212,258,266,0


```


## 7) Recommended generation presets

### Realistic run preset
- pick 1 layer from 101–106
- pick 0–1 layer from 301–306
- pick 1–2 layers from 401–406
- mirror each with 50% chance
- shift from set {-8,-4,0,+4,+8} with 50% chance else 0

### Abstract run preset
- pick 1 layer from 201–206
- pick 0–1 layer from 301–306
- pick 1–2 layers from 401–406
- same mirror/shift rules

### Mixed preset
- 50/50 choose structure from Realistic or Abstract
- optionally add one extra fence layer if difficulty is high
