# Wargus TypeScript Site Showcase (Approach B) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a polished Wargus TypeScript showcase image, then append a new product card on the Animas AI homepage and on tylermayberry.dev — never removing existing cards.

**Architecture:** Static HTML sites only. Produce one master showcase PNG from a real browser capture of the live demo (optional light polish), copy it into both repos, then patch each homepage to match existing card patterns. Portfolio supporting-grid CSS gains a sixth card in a multi-row layout (`milk | wargus` on the bottom row).

**Tech Stack:** Static HTML/CSS (Tailwind CDN on Animas; hand-rolled CSS on portfolio), Cloudflare Workers deploy (both sites auto-deploy from git), optional headless Chrome screenshot + Imagine `image_edit` for polish.

**Spec:** `docs/superpowers/specs/2026-08-06-wargus-portfolio-showcase-design.md`

## Global Constraints

- Live product URL is always `https://wargus.animasai.co`.
- **Append only:** never remove or replace Masthead, Pip, Executioner, Rat Detective, Milkbench, or any other existing card unless the user explicitly orders a removal.
- Animas scope is **homepage only** (`index.html` + asset). Do not edit `case-studies.html`, `resume.html`, or create `/wargus.html` in this plan.
- Portfolio deploy is **Cloudflare only** (`product-portfolio-preview` / tylermayberry.dev).
- Public copy must describe a **browser demo**, not a commercial product or full Wargus campaign suite.
- Do not claim multiplayer, full campaign, or source-perfect parity; the active product is the fixed Garden of War 1v1 demo.
- Prefer a **real demo capture** as the image base; do not invent fake HUD chrome that misrepresents the app.
- Canonical product name spelling: **Wargus TypeScript** (not “Worgus”).

---

## File map

### Repo A — Animas AI (this workspace: `/home/halla/workspaces/t3/animas-ai`)

| File | Role |
| --- | --- |
| `work-assets/wargus-typescript.png` | Create — homepage card image |
| `index.html` | Modify — selected-work card + any “selected work” count if present |

### Repo B — Portfolio (clone if missing: `MayberryDT/apps-portfolio`)

| File | Role |
| --- | --- |
| `Wargus.png` (repo root, next to `RatDetective.png`) | Create — card media used by `index.html` |
| `index.html` | Modify — intro copy, JSON-LD ItemList, supporting-grid CSS, new article |
| `AGENTS.md` | Create — append-only product rule for future agents |
| `README.md` | Optional one-line note if it lists the five products by count |

### Working artifacts (local only, do not commit secrets)

| Path | Role |
| --- | --- |
| `/tmp/wargus-demo-capture.png` | Raw browser screenshot |
| `/tmp/wargus-showcase-master.png` | Polished master before copying into repos |

---

### Task 1: Capture a real Garden of War demo frame

**Files:**
- Create (local only): `/tmp/wargus-demo-capture.png`
- Reference live: `https://wargus.animasai.co`

**Interfaces:**
- Consumes: live deploy of Wargus TypeScript
- Produces: readable 16:9-ish PNG of real in-game terrain/units/HUD

- [ ] **Step 1: Confirm the live demo responds**

```bash
curl -sI https://wargus.animasai.co | head -15
```

Expected: HTTP 200 (Cloudflare).

- [ ] **Step 2: Capture a playable frame with headless Chrome**

Prefer a real runtime frame over marketing art. From a machine with Chrome/Chromium:

```bash
# If playwright is available in Wargus repo:
cd /home/halla/workspaces/t3/Wargus-TypeScript
# Option A: reuse existing browser smoke if it writes screenshots under .artifacts
find .artifacts -name '*.png' 2>/dev/null | head -20

# Option B: one-shot Chromium screenshot after load
chromium --headless --disable-gpu --window-size=1440,900 \
  --screenshot=/tmp/wargus-demo-capture.png \
  "https://wargus.animasai.co" || \
google-chrome --headless --disable-gpu --window-size=1440,900 \
  --screenshot=/tmp/wargus-demo-capture.png \
  "https://wargus.animasai.co"
```

If the default load lands on a loading/splash state with no map, wait and re-capture:

```bash
# Playwright one-liner alternative (install only if needed)
npx --yes playwright install chromium
node --input-type=module <<'EOF'
import { chromium } from 'playwright';
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await page.goto('https://wargus.animasai.co', { waitUntil: 'networkidle', timeout: 120000 });
await page.waitForTimeout(8000); // allow map/assets to settle
await page.screenshot({ path: '/tmp/wargus-demo-capture.png', type: 'png' });
await browser.close();
console.log('wrote /tmp/wargus-demo-capture.png');
EOF
```

- [ ] **Step 3: Visually inspect the capture**

```bash
file /tmp/wargus-demo-capture.png
identify /tmp/wargus-demo-capture.png 2>/dev/null || true
```

Open/read the image. Accept only if it shows recognizable RTS content (terrain tiles, units or buildings, not a blank black canvas or pure loading spinner). If blank, re-run with a longer wait or local `npm run dev` + screenshot after interaction.

- [ ] **Step 4: Commit nothing yet**

Capture is local working material only.

---

### Task 2: Produce the polished showcase master asset

**Files:**
- Create (local): `/tmp/wargus-showcase-master.png`
- Create: `animas-ai/work-assets/wargus-typescript.png`
- Create (portfolio clone): `Wargus.png`

**Interfaces:**
- Consumes: `/tmp/wargus-demo-capture.png`
- Produces: shared master PNG used by both sites (≈16:9, strong contrast at card size)

- [ ] **Step 1: Decide polish path**

| Capture quality | Action |
| --- | --- |
| Strong composition, clear units, good contrast | Light crop + optional slight contrast via ImageMagick; skip generative edit |
| Usable but dull / awkward crop | `image_edit` with capture as reference: “tighten crop, raise contrast, keep true UI and art, portfolio product still” |
| Unusable | Fix capture (Task 1) before polish; do not invent a fake game UI from scratch |

- [ ] **Step 2: If using Imagine polish, edit from the real capture**

Use the harness image tools (not freehand fantasy art):

- Tool: `image_edit`
- `image`: `/tmp/wargus-demo-capture.png`
- Prompt (use or adapt):

```text
Polish this real browser screenshot of a Wargus TypeScript RTS demo into a clean portfolio product showcase still. Keep the authentic game terrain, units, buildings, and HUD. Improve crop to a cinematic 16:9 frame, raise contrast slightly, and keep text/UI legible. No fake logos, no invented menus, no people, no watermarks.
```

- Aspect: preserve capture unless multi-image edit needs `16:9`

- [ ] **Step 3: Export master and copy into Animas**

```bash
# After polish, ensure master exists:
cp /tmp/wargus-showcase-master.png \
  /home/halla/workspaces/t3/animas-ai/work-assets/wargus-typescript.png

# Or if capture is already good enough:
cp /tmp/wargus-demo-capture.png \
  /home/halla/workspaces/t3/animas-ai/work-assets/wargus-typescript.png

file /home/halla/workspaces/t3/animas-ai/work-assets/wargus-typescript.png
```

- [ ] **Step 4: Visually QA at card size**

Read the PNG with the image reader. Check:

- Not mostly empty / black
- Units or buildings visible
- Works as a wide card header (similar visual weight to `work-assets/rat-detective-online.png`)

Regenerate or re-crop once if needed.

- [ ] **Step 5: Commit Animas asset only after it is used by HTML, or commit asset with homepage in Task 3**

Prefer one commit in Task 3 that includes both image + HTML. No orphan asset commit required.

---

### Task 3: Add Wargus card to Animas AI homepage

**Files:**
- Modify: `index.html` (selected-work grid; insert near Rat Detective)
- Create/use: `work-assets/wargus-typescript.png`

**Interfaces:**
- Consumes: showcase PNG path `/work-assets/wargus-typescript.png`
- Produces: homepage article linking to `https://wargus.animasai.co`

- [ ] **Step 1: Locate the Rat Detective article in `index.html`**

```bash
rg -n "Rat Detective Online" index.html
```

Insert the new Wargus article **immediately after** the Rat Detective `</article>` (before Paycheck Sanity Checker). Pattern to mirror (dark playable card):

```html
          <article class="border border-gray-200 rounded-3xl bg-slate-950 overflow-hidden shadow-sm">
            <img src="/work-assets/wargus-typescript.png" alt="Wargus TypeScript browser RTS demo showing Garden of War gameplay" class="w-full aspect-[16/9] object-cover border-b border-white/10">
            <div class="p-7">
              <div class="inline-flex px-3 py-1 rounded-full bg-white/10 text-amber-200 text-xs font-bold uppercase tracking-wide mb-4">Playable RTS demo</div>
              <h3 class="font-display text-3xl font-bold tracking-tight text-white mb-3">Wargus TypeScript</h3>
              <p class="text-slate-300 leading-relaxed mb-5">A browser-native TypeScript/PixiJS port of Wargus gameplay. Fixed Garden of War 1v1 demo: harvest, train, build, and fight without a desktop engine install.</p>
              <a href="https://wargus.animasai.co" target="_blank" class="inline-flex items-center gap-2 font-bold text-white hover:text-amber-200">Play live <span class="material-symbols-outlined text-base">open_in_new</span></a>
            </div>
          </article>
```

- [ ] **Step 2: Verify markup balance**

```bash
# Quick sanity: card strings present
rg -n "Wargus TypeScript|wargus-typescript.png|wargus.animasai.co" index.html
```

Expected: title, image path, live URL each appear.

- [ ] **Step 3: Local visual check (optional static server)**

```bash
cd /home/halla/workspaces/t3/animas-ai
python3 -m http.server 8765
# open http://127.0.0.1:8765/ and scroll to selected work
```

Confirm card image loads, link target is correct, dark card matches neighbors.

- [ ] **Step 4: Commit Animas homepage + asset**

```bash
cd /home/halla/workspaces/t3/animas-ai
git status
git add work-assets/wargus-typescript.png index.html \
  docs/superpowers/specs/2026-08-06-wargus-portfolio-showcase-design.md \
  docs/superpowers/plans/2026-08-06-wargus-portfolio-showcase.md
git commit -m "$(cat <<'EOF'
feat: add Wargus TypeScript to homepage selected work

Showcase the browser RTS demo with a polished capture and
a new playable-product card linking to wargus.animasai.co.
EOF
)"
```

Do **not** push unless the user asks.

---

### Task 4: Clone portfolio repo and drop in showcase image

**Files:**
- Clone: `MayberryDT/apps-portfolio` (if not already local)
- Create: `Wargus.png` at repo root (same level as `RatDetective.png`, `Milkbench.png`)

**Interfaces:**
- Consumes: master showcase from Task 2
- Produces: portfolio-relative image `Wargus.png` referenced by `index.html`

- [ ] **Step 1: Clone beside Animas (or reuse existing clone)**

```bash
# Preferred location on Halla:
cd /home/halla/workspaces/t3
if [ ! -d apps-portfolio ]; then
  git clone git@github.com:MayberryDT/apps-portfolio.git
fi
cd apps-portfolio
git status
git checkout master
git pull --ff-only
```

- [ ] **Step 2: Copy showcase asset**

```bash
cp /home/halla/workspaces/t3/animas-ai/work-assets/wargus-typescript.png \
  /home/halla/workspaces/t3/apps-portfolio/Wargus.png
file Wargus.png
```

- [ ] **Step 3: Confirm existing five cards still present before editing**

```bash
rg -n "Masthead|Pip|Executioner|Rat Detective|Milkbench" index.html | head -40
```

Expected: all five still in HTML. Do not delete any.

---

### Task 5: Update portfolio supporting-grid layout for six products

**Files:**
- Modify: `apps-portfolio/index.html` (CSS block for `.supporting-grid` and mobile breakpoint)

**Interfaces:**
- Consumes: existing named grid areas `pip`, `executioner`, `rat`, `milk`
- Produces: new area `wargus`; desktop layout is multi-row, not one row of five

- [ ] **Step 1: Replace desktop supporting-grid template**

Find the current block (live as of 2026-08-06):

```css
.supporting-grid {
    grid-template-columns: minmax(0, 1.15fr) minmax(280px, 0.85fr);
    grid-template-areas:
        "pip executioner"
        "rat rat"
        "milk milk";
    align-items: start;
}
```

Replace with:

```css
.supporting-grid {
    grid-template-columns: minmax(0, 1.15fr) minmax(280px, 0.85fr);
    grid-template-areas:
        "pip executioner"
        "rat rat"
        "milk wargus";
    align-items: start;
}
```

- [ ] **Step 2: Add CSS for the new card class**

After `.supporting-grid .project.milk-card { ... }` add:

```css
.supporting-grid .project.wargus-card {
    grid-area: wargus;
    grid-template-columns: minmax(0, 1.05fr) minmax(300px, 0.95fr);
    grid-template-rows: auto;
}

.supporting-grid .project.wargus-card .project-media img {
    width: 100%;
    height: 100%;
    min-height: 220px;
    object-fit: cover;
    object-position: center;
}
```

(Match exact image rules used by `.milk-card` / `.rat-card` in the same file if they differ — copy those values rather than inventing new ones.)

- [ ] **Step 3: Update mobile grid areas (`max-width: 980px`)**

Replace:

```css
.supporting-grid {
    grid-template-rows: auto;
    grid-template-areas:
        "pip"
        "executioner"
        "rat"
        "milk";
}
```

with:

```css
.supporting-grid {
    grid-template-rows: auto;
    grid-template-areas:
        "pip"
        "executioner"
        "rat"
        "milk"
        "wargus";
}
```

And force single-column interior for the new card:

```css
.supporting-grid .project.wargus-card {
    grid-area: wargus;
    grid-template-columns: 1fr;
}
```

- [ ] **Step 4: Spot-check CSS names**

```bash
rg -n "grid-template-areas|wargus-card|milk-card" index.html
```

Expected: `wargus` in both desktop and mobile area maps; `.wargus-card` defined.

---

### Task 6: Append portfolio Wargus card + copy/schema updates

**Files:**
- Modify: `apps-portfolio/index.html` (HTML card, intro blurb, JSON-LD ItemList)
- Create: `apps-portfolio/AGENTS.md`
- Optional: `README.md` if it hardcodes “five”

**Interfaces:**
- Consumes: `Wargus.png`, `.wargus-card` styles from Task 5
- Produces: sixth project card; schema position 6; append-only agent rule

- [ ] **Step 1: Update work-section intro copy**

Find:

```html
<p>A focused index of five current public products: Masthead, Pip, Executioner, Rat Detective, and Milkbench.</p>
```

Replace with:

```html
<p>A focused index of current public products: Masthead, Pip, Executioner, Rat Detective, Milkbench, and Wargus TypeScript.</p>
```

- [ ] **Step 2: Extend JSON-LD ItemList**

Find the `ItemList` entries (positions 1–5). Append:

```json
{ "@type": "ListItem", "position": 6, "name": "Wargus TypeScript", "url": "https://wargus.animasai.co" }
```

Keep positions 1–5 unchanged.

- [ ] **Step 3: Append the article after Milkbench (still inside `.supporting-grid`)**

```html
                <article class="project wargus-card">
                    <a class="cover-link" href="https://wargus.animasai.co" target="_blank" rel="noopener noreferrer" aria-label="Open Wargus TypeScript"></a>
                    <div class="project-media">
                        <img src="Wargus.png" alt="Wargus TypeScript browser RTS demo on Garden of War" loading="lazy">
                    </div>
                    <div class="project-body">
                        <div class="project-meta">
                            <span class="status game">Live demo</span>
                            <span class="domain">Browser RTS</span>
                        </div>
                        <div>
                            <h3>Wargus TypeScript</h3>
                            <p>Browser-native TypeScript/PixiJS port of Wargus gameplay. Fixed Garden of War 1v1 demo with harvest, production, and combat in the browser.</p>
                        </div>
                        <span class="open">Open demo →</span>
                    </div>
                </article>
```

- [ ] **Step 4: Confirm no existing card was removed**

```bash
rg -n "<h3>Masthead</h3>|<h3>Pip</h3>|<h3>Executioner</h3>|<h3>Rat Detective Online</h3>|<h3>Milkbench</h3>|<h3>Wargus TypeScript</h3>" index.html
```

Expected: six headings, all present.

- [ ] **Step 5: Create `AGENTS.md` with append-only rule**

```markdown
# Agent notes — apps-portfolio

## Product cards

- The homepage is a curated product index (featured Masthead + supporting cards).
- **When asked to add a product: always append a new card.** Never remove or replace an existing card unless the user explicitly requests removal.
- Prefer multi-row CSS grid areas over dumping every card into one horizontal row.
- Live Wargus TypeScript URL: https://wargus.animasai.co
- Deploy: Cloudflare Worker custom domains for tylermayberry.dev only.

## Current supporting cards (as of 2026-08-06)

1. Pip
2. Executioner
3. Rat Detective Online
4. Milkbench
5. Wargus TypeScript
```

- [ ] **Step 6: Local preview**

```bash
cd /home/halla/workspaces/t3/apps-portfolio
python3 -m http.server 8766
# open http://127.0.0.1:8766/
```

Check: six products, bottom row is milk | wargus on desktop, stack on narrow viewport, image loads, cover-link hits wargus.animasai.co.

- [ ] **Step 7: Commit portfolio**

```bash
cd /home/halla/workspaces/t3/apps-portfolio
git add Wargus.png index.html AGENTS.md
git status
git commit -m "$(cat <<'EOF'
feat: add Wargus TypeScript as sixth portfolio product

Append a live-demo card with showcase art, extend the supporting
grid into a multi-row layout, and record the append-only card rule.
EOF
)"
```

Do **not** push unless the user asks.

---

### Task 7: Cross-site verification and handoff

**Files:**
- None required (read-only verification)
- Optional GBrain closeout under `sessions/2026/08/` if durable

**Interfaces:**
- Consumes: both local trees after Tasks 3–6
- Produces: verification checklist result for the user

- [ ] **Step 1: Animas regression checklist**

```bash
cd /home/halla/workspaces/t3/animas-ai
test -f work-assets/wargus-typescript.png && echo "asset ok"
rg -n "wargus.animasai.co|Wargus TypeScript" index.html
# Ensure case studies untouched:
rg -n "Wargus" case-studies.html || echo "case-studies clean (expected)"
```

- [ ] **Step 2: Portfolio regression checklist**

```bash
cd /home/halla/workspaces/t3/apps-portfolio
test -f Wargus.png && echo "asset ok"
rg -n "Wargus TypeScript|wargus.animasai.co|wargus-card" index.html
rg -n "append a new card|Never remove" AGENTS.md
# five originals still present:
rg -c "Masthead|Pip|Executioner|Rat Detective|Milkbench" index.html
```

- [ ] **Step 3: Report to user**

Include:

1. Paths of commits (hashes) in both repos  
2. Local preview URLs used  
3. Note that production updates require push + Cloudflare auto-deploy  
4. Offer push/PR if they want it

- [ ] **Step 4: Optional durable closeout (GBrain)**

If GBrain is available, write a short session note:

- What shipped (homepage + portfolio cards + append-only rule)
- Live URL `https://wargus.animasai.co`
- Spec/plan slugs under `docs/superpowers/`

---

## Self-review (plan vs spec)

| Spec requirement | Task |
| --- | --- |
| Polished showcase image first | Tasks 1–2 |
| Animas homepage only | Task 3 |
| Portfolio new card append-only | Tasks 4–6 |
| Multi-row layout, not one flat row | Task 5 (`milk \| wargus`) |
| Schema + “five” copy update | Task 6 |
| AGENTS.md standing rule | Task 6 |
| No case studies / no dedicated page | Explicit non-goals; Task 7 checks case-studies clean |
| Correct product URL | All HTML samples use `https://wargus.animasai.co` |

Placeholder scan: no TBD/TODO steps remaining.  
Naming consistency: card class `wargus-card`, image `Wargus.png` / `wargus-typescript.png`, product name **Wargus TypeScript**.

---

## Out of scope reminders for implementers

- Do not edit Wargus game source for this plan.
- Do not remove Milkbench or Rat Detective to “make room.”
- Do not update `resume.html` unless a follow-up task asks.
