# Driveway Shoveler (Model 100 BASIC) — Wall Templates (Levels 1–5)

This note describes a **compact** way to store and load **wall-only** obstacle templates for an **8×40** board, and the minimal code changes needed to integrate **Level Select (1–5)** into the current program.

## Design recap (for this phase)
- Board size: **8 rows × 40 columns**
- Walls only (`#`). No mailbox/special tiles.
- Keep your current snow rules as implemented (whole-block push, lawn cap 5, driveway cap 3).
- Win condition can remain: **player reaches col 40**.
- Walls must:
  - block movement
  - block pushing (you cannot push snow into/through a wall)
  - visually override snow when drawn

---

## Compact template storage format

Instead of storing 8 strings × 40 chars per level, store only the wall cells as a list of **linear indices**.

### Linear index definition
For row `r` (1..8) and column `c` (1..40):

- `idx = (r-1)*40 + c`  (range 1..320)

Each level stores a DATA list of the wall indices, terminated with `0`.

Example:
- A single wall at row 2 col 20 → `idx = (2-1)*40 + 20 = 60`
- DATA: `60,0`

This is compact and fast to load.

---

## Code changes (minimal)

### 1) Add obstacle array + level variable

Change:
```basic
30 DIM S%(9,41)
```

To:
```basic
30 DIM S%(9,41),O%(9,41)
```

Add a global:
- `LEVEL%` set by the Level Select screen.

---

### 2) Call template loader at start + restart

After Level Select, load the template before `INIT`:

```basic
80 GOSUB 1500
82 GOSUB 8000  'LOAD TEMPLATE LEVEL% -> O%()
85 GOSUB 500
90 GOSUB 600
```

On restart key:
```basic
140 IF K$="R" OR K$="r" THEN GOSUB 8000:GOSUB 500:GOSUB 600:GOTO 110
```

In WIN handler restart:
```basic
1240 IF K$="R" OR K$="r" THEN GOSUB 8000:GOSUB 500:GOSUB 600:GOTO 110
```

---

### 3) Block movement into walls

Update your movement test line to include `O%`:

```basic
220 IF NR%<2 OR NR%>7 OR O%(NR%,NC%)<>0 OR S%(NR%,NC%)<>0 THEN 240
```

---

### 4) Block pushing into/through walls

Before pushing, ensure the adjacent snow tile is not a wall (defensive), and the destination is not a wall:

```basic
240 IF O%(NR%,NC%)<>0 THEN 110
242 IF S%(NR%,NC%)<=0 THEN 110
250 TR%=NR%+RS%:TC%=NC%+CS%
260 IF TR%<1 OR TR%>8 OR TC%<1 OR TC%>40 THEN 110
265 IF O%(TR%,TC%)<>0 THEN 110
```

Keep the rest of your shove logic as-is.

---

### 5) Draw walls (walls override snow)

In your cell draw routine `700`, insert:

```basic
715 IF O%(RR%,CC%)<>0 THEN CH$="#":RV%=0:GOTO 770
```

Recommended ordering:

```basic
710 PO%=(RR%-1)*40+(CC%-1)
712 IF RR%=PR% AND CC%=PC% THEN CH$=CHR$(147):RV%=0:GOTO 770
715 IF O%(RR%,CC%)<>0 THEN CH$="#":RV%=0:GOTO 770
```

---

### 6) Clear snow values under walls after INIT

At the end of `INIT` (sub 500), add:

```basic
585 FOR R%=1 TO 8
586 FOR C%=1 TO 40
587 IF O%(R%,C%)<>0 THEN S%(R%,C%)=0
588 NEXT C%
589 NEXT R%
```

This prevents “hidden snow” inside wall tiles from affecting pushes.

---

## Level Select (pick 1–5)

Replace your `1500` routine with:

```basic
1500 REM LEVEL SELECT
1510 CLS
1520 PRINT " LEVEL SELECT"
1530 PRINT
1540 PRINT " 1. LEVEL 1"
1550 PRINT " 2. LEVEL 2"
1560 PRINT " 3. LEVEL 3"
1570 PRINT " 4. LEVEL 4"
1580 PRINT " 5. LEVEL 5"
1590 PRINT
1600 PRINT " SELECT (1-5) OR Q"
1610 K$=INKEY$:IF K$="" THEN 1610
1620 IF K$="Q" OR K$="q" THEN CLEAR:CLS:END
1630 IF K$>="1" AND K$<="5" THEN LEVEL%=VAL(K$):RETURN
1640 GOTO 1610
```

---

## Template loader subroutine (compact index lists)

Add this new subroutine:

```basic
8000 REM LOAD TEMPLATE LEVEL% INTO O%() USING INDEX LISTS
8010 FOR R%=1 TO 8
8020 FOR C%=1 TO 40
8030 O%(R%,C%)=0
8040 NEXT C%
8050 NEXT R%

8060 IF LEVEL%=1 THEN RESTORE 9000
8070 IF LEVEL%=2 THEN RESTORE 9100
8080 IF LEVEL%=3 THEN RESTORE 9200
8090 IF LEVEL%=4 THEN RESTORE 9300
8100 IF LEVEL%=5 THEN RESTORE 9400

8110 READ IDX%
8120 IF IDX%=0 THEN RETURN
8130 R%=(IDX%-1)\40+1
8140 C%=((IDX%-1) MOD 40)+1
8150 O%(R%,C%)=1
8160 GOTO 8110
```

Notes:
- Uses integer math: `\` is integer division in many BASICs; if Model 100 BASIC requires `INT((IDX%-1)/40)` then use that instead:
  - `R%=INT((IDX%-1)/40)+1`

---

## Wall templates (Levels 1–5)

Each list is wall cell indices terminated by `0`.

### Level 1 — single post line
Walls at col 20 in rows 2,3,5,6,7.

```basic
9000 DATA 60,100,180,220,260,0
```

### Level 2 — two staggered post columns
```basic
9100 DATA 54,67,107,134,174,187,227,254,0
```

### Level 3 — horizontal fence with one opening
Row 5 has a long fence with a 1-cell gap.

```basic
9200 DATA 168,169,170,171,172,173,174,175,176,177,178,179,181,182,183,184,185,186,187,188,189,190,191,192,193,0
```

### Level 4 — central island box
```basic
9300 DATA 98,99,100,101,102,103,138,143,178,183,218,219,220,221,222,223,0
```

### Level 5 — serpentine posts
```basic
9400 DATA 50,60,70,90,110,140,170,180,190,210,260,270,0
```

---

## Sanity checks after integration
1) You cannot move into `#`.
2) You cannot push snow into `#`.
3) Walls render as `#` even if snow values exist there (they should be cleared anyway).
4) Level Select picks 1–5 and loads the correct template.
5) Restart reloads the same selected level.

