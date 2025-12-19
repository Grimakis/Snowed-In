# Codex Doc: Nicer Menus (Borders + Centered Text + Version v0.1.0)
*(TRS-80 Model 100 BASIC, 40×8 screen, uses PRINT@)*

This document upgrades the **Title screen** (`6000`) and **Level Select menu** (`7000`) to look more elegant:
- A **bordered panel**
- **Properly centered text**
- A displayed **version number: v0.1.0**
- Simple, reusable helpers: `DRAWBOX` and `CENTERPRINT`

All code below is Model 100 BASIC-friendly and avoids fancy characters that might not render consistently.

---

## 1) Add constants + version string
Add near the top (after DIMs):

```basic
1090 VER$="v0.1.0"
1092 SW%=40:SH%=8
```

If you prefer not to add SW%/SH%, you can hardcode 40 and 8 in the helper subs.

---

## 2) Add helper subroutines

### 2.1 DRAWBOX (simple ASCII border)
Draws a rectangle border using `+ - |`.

Inputs (globals):
- `BR%` top row (1..8)
- `BC%` left col (1..40)
- `BH%` height in rows
- `BW%` width in cols

```basic
5600 REM DRAWBOX BR%,BC%,BH%,BW%
5610 T%=BR%:L%=BC%:H%=BH%:W%=BW%
5620 IF H%<2 OR W%<2 THEN RETURN
5630 REM TOP EDGE
5640 PO%=(T%-1)*40+(L%-1):PRINT@PO%,"+";
5650 FOR I%=1 TO W%-2:PRINT@PO%+I%,"-";:NEXT I%
5660 PRINT@PO%+W%-1,"+";

5670 REM SIDES
5680 FOR R%=T%+1 TO T%+H%-2
5690 PO%=(R%-1)*40+(L%-1):PRINT@PO%,"|";
5700 PRINT@PO%+W%-1,"|";
5710 NEXT R%

5720 REM BOTTOM EDGE
5730 R%=T%+H%-1
5740 PO%=(R%-1)*40+(L%-1):PRINT@PO%,"+";
5750 FOR I%=1 TO W%-2:PRINT@PO%+I%,"-";:NEXT I%
5760 PRINT@PO%+W%-1,"+";
5770 RETURN
```

### 2.2 CENTERPRINT (centers a string on a row, inside an optional box)
Inputs:
- `CR%` row (1..8)
- `TXT$` text to print
- `CL%` left boundary column (default 1)
- `CW%` width boundary (default 40)

Prints using `PRINT@` so it doesn’t scroll.

```basic
5800 REM CENTERPRINT CR%,TXT$,CL%,CW%
5810 IF CL%<1 THEN CL%=1
5820 IF CW%<1 THEN CW%=40
5830 LN%=LEN(TXT$)
5840 IF LN%>CW% THEN TXT$=LEFT$(TXT$,CW%):LN%=CW%
5850 COL%=CL%+INT((CW%-LN%)/2)
5860 PO%=(CR%-1)*40+(COL%-1)
5870 PRINT@PO%,TXT$;
5880 RETURN
```

Tip: Before calling, set `CL%` and `CW%` to the *inside* width of your box (e.g., box left+1, box width-2).

---

## 3) Replace Title Screen (6000) with a centered bordered panel

Replace your `6000` block with:

```basic
6000 REM TITLE SCREEN (POLISHED)
6020 CLS
6030 BR%=1:BC%=1:BH%=8:BW%=40:GOSUB 5600

6040 CL%=2:CW%=38
6050 CR%=2:TXT$="SNOW DAY":GOSUB 5800
6060 CR%=3:TXT$="DRIVEWAY SHOVELER":GOSUB 5800
6070 CR%=4:TXT$="BY GEORGE M. RIMAKIS":GOSUB 5800

6080 CR%=6:TXT$="PRESS ANY KEY":GOSUB 5800
6090 CR%=7:TXT$=VER$:GOSUB 5800

6100 K$=INKEY$:IF K$="" THEN 6100
6110 RETURN
```

---

## 4) Upgrade Level Select Menu (7000) with a bordered panel + clean layout

### 4.1 Replace the menu draw section
In your `7000` block, replace the `7120` menu drawing section with:

```basic
7120 CLS
7130 BR%=1:BC%=1:BH%=8:BW%=40:GOSUB 5600
7140 CL%=2:CW%=38

7150 CR%=2:TXT$="LEVEL SELECT":GOSUB 5800

7160 SM$="OFF":IF SM%=1 THEN SM$="LIGHT"
7170 IF SM%=2 THEN SM$="MED"
7180 IF SM%=3 THEN SM$="HEAVY"

7190 REM OPTION ROWS
7200 PRINT@80,"   DRIVEWAY LVL: ";LL%;"   ";
7210 PRINT@120,"   SNOW MODE   : ";SM$;"   ";

7220 REM SELECTOR
7230 IF MT%=1 THEN PRINT@80,">" ELSE PRINT@120,">"

7240 REM FOOTER
7250 CR%=7:TXT$="ENTER=START   Q=QUIT":GOSUB 5800
7260 CR%=8:TXT$=VER$:GOSUB 5800
7270 GOTO 7360
```

Notes:
- `PRINT@80` is row 3 col 1 (since (3-1)*40=80)
- `PRINT@120` is row 4 col 1

If you want a tighter panel (not full screen), use:
- `BR%=1:BC%=2:BH%=8:BW%=38`
and set `CL%=3:CW%=36`.

---

## 5) Optional: Faster selector movement (later)
Full redraw is simplest and still looks good. If you want snappier movement later, Codex can:
- clear the old `>` with `PRINT@` and redraw only the arrow on up/down,
- only full redraw when LL%/SM% values change.

---

## 6) Checklist
1) Add `VER$="v0.1.0"` near the top.
2) Add `5600 DRAWBOX` and `5800 CENTERPRINT`.
3) Replace `6000` with the polished title screen.
4) Replace the menu drawing block under `7000` with the bordered, centered version.

