# Fixing Mini-Templates (Layered Wall Pieces) So Most Generated Maps Are Winnable
*(TRS-80 Model 100 BASIC, 8×40 board, walls-only obstacle layer)*

This document explains **how to redesign “mini-templates” (layers)** so they combine well (with mirroring/shifting) and produce **mostly winnable** layouts. It also defines the **validation gates** that should be applied during generation.

never use variable names larger than 2 plus sigil and never use a Keyword like OR

---

## 0) Why your current layered maps became unwinnable
Layered wall systems fail when any of these happen:

1) **Too much wall density** once 2–4 layers overlap.
2) Layers create **wide cross-driveway barriers** (even if no single column is fully blocked).
3) Mirroring/shift causes multiple layers to stack in the same choke region.
4) Validation only checks “no solid wall column,” but does **not check connectivity**.

Key idea: **Snow is movable, walls are not.**  
If the open driveway graph is disconnected by walls, the level is unwinnable regardless of snow.

---

## 1) Target: “Additive-safe” layers
A layer is *additive-safe* if it can be OR-combined with 1–2 other layers (plus optional mirror/shift) and still usually leaves at least one open route from left to right.

To make layers additive-safe, enforce these structural rules when designing them.

---

## 2) Hard design constraints for each mini-template

### 2.1 Protected columns (spawn/finish zones)
Never place walls in:
- **Spawn zone:** columns **1–3**
- **Finish zone:** columns **38–40** *(or 37–39 if your goal is col 39)*

These zones provide maneuver space and prevent accidental “gates” that are too tight.

**Rule for all layers:** any wall cell whose column falls in a protected zone should be removed from the layer (or skipped at apply-time).

### 2.2 Limit vertical coverage per column
A single column with walls in many rows is dangerous.

For each layer:
- In any column, the number of blocked driveway rows (2–7) should be **≤ 3**.
- Avoid patterns like a full 5–6 cell vertical fence (even with a gap).

### 2.3 Limit horizontal run length
Long horizontal bars are the easiest way to sever the map.

For each layer:
- Maximum contiguous horizontal run in a single driveway row should be **≤ 6** (prefer ≤ 4).
- If you use longer runs, ensure **multiple gaps**, not a single gap.

### 2.4 Avoid “single-tile gates”
A single open cell that every route must pass through is a soft fail: it becomes jammy and often practically impossible.

When a layer creates a choke:
- Make the choke **2 tiles wide** (two adjacent open cells in the same column or row).
- Or provide a second alternate route around.

### 2.5 Keep most layers small
Treat layers as “spice,” not “wallpaper.”

Recommended wall counts per layer (driveway rows only):
- **Post layer:** 3–6 walls
- **Fence layer:** 6–10 walls
- **Structure layer:** 8–14 walls *(only one structure per level recipe)*

If a structure has 20+ walls, it’s a *full template*, not a mini-template.

---

## 3) Classify layers so the generator doesn’t make “brick soup”
Don’t pick layers uniformly. Categorize them and restrict combinations.

### 3.1 Layer categories
- **POST:** sparse single tiles (very safe)
- **FENCE:** short segments / mini barriers (moderate risk)
- **STRUCTURE:** “islands,” shapes, boxes (higher risk)

### 3.2 Recommended recipe constraints
Use recipes like these:

**Easy (high win rate):**
- 1 STRUCTURE (small)
- + 1 POST
- (no FENCE)

**Medium:**
- 1 STRUCTURE
- + 1 POST
- + optional 1 FENCE (only if structure is tiny)

**Hard:**
- 1 STRUCTURE
- + 1 FENCE
- + 1 POST  
Plus strict validation.

**Never:**
- 2 STRUCTURE layers in the same level
- 2 long FENCE layers together

---

## 4) Mirroring and shifting: constrain it
Mirroring is usually safe. Shifting is where disasters happen.

### 4.1 Mirror (horizontal)
Good. Keep it.

### 4.2 Shift
If you allow shift, restrict it:
- allowed shifts: `{ -6, -3, 0, +3, +6 }`
- only apply shift to POST layers (not STRUCTURE/FENCE) initially

### 4.3 Collision control
If two layers overlap heavily, you increase local density.

Add a cheap collision metric during generation:
- Count overlaps where `O%` is already 1 and a new layer tries to place another wall.
- If overlaps exceed a threshold (e.g., `OVERLAPS% > 3`), reject and reroll.

---

## 5) Add real validation: connectivity on the obstacle grid
Your validation must check:
> Is there at least one open left-to-right route through driveway cells (rows 2–7) ignoring snow?

### 5.1 Connectivity check (must-have)
Run BFS/DFS on open cells where `O%(r,c)=0`.

- Start nodes: `(r,1)` for `r=2..7` where open
- Goal nodes: `(r,40)` *(or goal column)* for `r=2..7` where open
- 4-way adjacency (N/S/E/W)
- If no path exists: **reject this combined layout** and reroll.

This alone turns “mostly unwinnable” into “mostly okay.”

### 5.2 Secondary checks (cheap and helpful)
- **Wall budget:** total walls in driveway rows 2–7 must be ≤ MAXWALLS%
  - Easy: 10–12
  - Medium: 14–16
  - Hard: 18–20
- **Spawn column open:** at least one open cell in col 1 rows 2–7
- **Goal column open:** at least one open cell in goal column rows 2–7
- **No fully blocked columns** (still keep this check, but it’s not sufficient alone)

---

## 6) How to redesign your existing mini-templates
Use this systematic process:

### Step A: Measure each layer
For each layer:
- count total driveway walls
- compute max walls per column
- compute max horizontal run per row
- list which columns are touched (avoid protected zones)

### Step B: Trim the “bad” features
Fix in this order:
1) Remove anything in protected zones
2) Break long horizontal runs with extra gaps
3) Reduce vertical fences (max 3 walls per column)
4) Remove “box fills” (turn solid rectangles into outlines, or smaller islands)
5) Reduce total wall count to target range

### Step C: Test layer in combinations
Write a small generator test harness:
- Generate 200 random level mixes using your recipe
- Count % passing connectivity check
- Also compute average wall count

Goal: **≥ 90%** of generated layouts pass connectivity at Easy recipe.

If a single layer causes many rejects, that layer is not additive-safe. Reduce it or remove it.

---

## 7) Recommended “safe” mini-template patterns (examples)
These are **concept shapes** that tend to combine well:

### POST patterns
- “Four corners” (4 posts scattered)
- “Diagonal sprinkle” (5 posts in a gentle diagonal)
- “Two pairs” (2 posts near left-mid, 2 near right-mid)

### FENCE patterns (short)
- “Broken bar” (8 long but with 2–3 gaps)
- “Staggered pillars” (two short vertical segments separated by several rows)

### STRUCTURE patterns (small)
- “Tiny island” (2×3 or 3×3 solid)
- “Cove” (U-shape with a wide mouth)
- “Hollow mini-box” (outline, not filled)

Avoid: full-width fences, large filled rectangles, single-gap long fences.

---

## 8) Practical generator defaults (recommended starting point)
To quickly get winnable layered levels:

- Use only **POST + small STRUCTURE** at first.
- Disable shift for STRUCTURE/FENCE.
- Use MAXWALLS% = 12 (Easy), 16 (Medium).
- Enforce protected zones.
- Enforce connectivity BFS.

Once you’re happy with win rates, gradually add:
- 1 fence layer
- shift for post layers only
- harder wall budgets

---

## 9) “Done” criteria for mini-template library
Your library is “good” when:

- Easy recipe: ≥ 90% candidate mixes pass connectivity without rerolls
- Medium recipe: ≥ 75% pass
- Hard recipe: ≥ 50% pass (rerolls acceptable)
- Playtests rarely produce obvious unwinnable barriers

---

## 10) TL;DR checklist
When editing or adding a mini-template, confirm:

- [ ] No walls in columns 1–3 or 38–40
- [ ] ≤ 3 walls in any column
- [ ] No horizontal run > 6 without multiple gaps
- [ ] Wall count matches its category (post/fence/structure)
- [ ] Generator uses category recipes (no structure stacking)
- [ ] Generator validates connectivity (BFS) and wall budget
- [ ] Mirror always allowed; shift restricted (especially early)
