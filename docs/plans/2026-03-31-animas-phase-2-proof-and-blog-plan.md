# Animas AI Phase 2 Proof and Blog Refresh Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Rewrite the case studies page around the new consulting-firm speed-to-lead positioning, refresh the blog index so it supports the new site narrative, and publish a small set of new blog articles that actually match the current ICP and wedge while keeping the older hotel and OpenClaw articles live on their existing URLs.

**Architecture:** Keep the current static HTML structure and visual system. Rewrite `case-studies.html` completely with new narrative-driven case studies, including Brander Group. Rewrite `blog/index.html` so it features only new consulting-firm workflow articles. Leave the legacy blog post files in place, but remove them from the featured blog grid so they remain crawlable and indexable without polluting the main funnel.

**Tech Stack:** Static HTML files with Tailwind via CDN, direct per-page metadata, hand-authored article pages under `blog/`, shared nav/footer patterns.

---

## Phase 2 Scope

### In scope
- Full rewrite of `case-studies.html`
- New proof framing and metadata for case studies
- Full rewrite of `blog/index.html`
- Creation of a small set of new blog articles aligned to the current ICP
- Removal of legacy hotel and OpenClaw posts from the blog landing page grid only
- CTA and metadata consistency across phase 2 assets

### Out of scope
- Deleting old blog post files
- Rewriting old hotel and OpenClaw blog articles
- Changing the current homepage, how-it-works page, or solutions page unless a small consistency fix is required
- Large design system changes

---

## Strategic Rules for Phase 2

1. **Case studies must support the wedge.**
   The page should make a consulting-firm buyer think, "These people solve revenue-adjacent workflow problems fast."

2. **Use Brander Group as a real anchor case.**
   Draft strong copy now. Tyler will tune factual accuracy afterward.

3. **The blog index is a curation layer, not an archive dump.**
   Keep legacy articles on the site, but do not feature them on the main blog page if they confuse the new ICP.

4. **New blog posts should support the current sales motion.**
   They should make the speed-to-lead wedge feel obvious, not experimental.

5. **Do not drift back into broad AI-agency language.**
   Every asset should reinforce: founder-led consulting firms, lead handling pain, one workflow first, Tyler owns workflow design and implementation.

---

## Target Outputs

### Rewritten page
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/case-studies.html`

### Rewritten blog index
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/index.html`

### New blog articles
Create 4 new posts to start:
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/speed-to-lead-consulting-firms.html`
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/lead-handling-vs-lead-generation.html`
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/how-founder-led-firms-lose-leads-in-the-handoff.html`
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/what-a-7-day-speed-to-lead-sprint-actually-fixes.html`

Optional later additions:
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/proposal-and-onboarding-bottlenecks.html`
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/client-reporting-workflow-drag.html`

### Legacy posts to keep live but remove from main blog grid
Keep these files untouched and accessible:
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/hotel-win-channel-intro.html`
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/ai-agents-hospitality-future.html`
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/openclaw-for-hotel-owners.html`
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/openclaw-cloud-architecture.html`
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/openclaw-google-workspace-setup.html`

---

## Page Design Direction

### Case studies page structure
1. Hero
2. Short framing section about fixing one workflow first
3. Brander Group case study
4. Case study two focused on speed-to-lead style workflow transformation
5. Case study three focused on adjacent workflow expansion
6. Short "how Animas works" proof bridge
7. Final CTA

### Blog index structure
Keep the current overall structure, but rewrite the content blocks:
1. Hero explaining what the blog is for now
2. Optional short note that this is writing about workflow design, lead handling, and operational bottlenecks for consulting firms
3. Grid of only the new aligned posts
4. Final CTA back to workflow audit

### Individual blog article structure
1. Headline
2. Short dek/subheadline
3. Article body with strong section headers
4. Practical examples
5. Final CTA back to workflow audit or speed-to-lead conversation

---

## Content Direction for Case Studies

### Case Study 1: Brander Group
**Role:** anchor proof piece

**Narrative shape:**
- Challenge: operational drag and manual handling across a high-friction workflow
- Intervention: Tyler mapped the workflow, designed the system, and implemented automation to remove repetitive manual work and improve throughput
- Result: meaningful time savings, less manual handling, better consistency, faster internal execution

**Important:**
Do not overfit Brander Group to consulting-firm lead handling if the actual work was broader. Instead, frame it as proof that Tyler can own workflow design and implementation end to end.

### Case Study 2: Speed-to-lead style transformation
**Role:** direct wedge proof

This can be written as a consulting-firm style lead handling case. Tyler will later adjust specifics. The page needs at least one proof block that feels tightly aligned to the current offer.

### Case Study 3: Adjacent workflow expansion
**Role:** show the expansion path after the first workflow win

This should support the core GTM logic:
- start with one urgent workflow
- prove value fast
- expand into deeper systems work

---

## Content Direction for New Blog Posts

### Post 1
**File:** `blog/speed-to-lead-consulting-firms.html`

**Working title:**
Why speed to lead matters more than most consulting firms think

**Purpose:**
Top-of-funnel thought leadership tied directly to the wedge.

### Post 2
**File:** `blog/lead-handling-vs-lead-generation.html`

**Working title:**
Most consulting firms do not have a lead gen problem. They have a lead handling problem.

**Purpose:**
Directly reinforce the homepage thesis.

### Post 3
**File:** `blog/how-founder-led-firms-lose-leads-in-the-handoff.html`

**Working title:**
How founder-led consulting firms lose good leads in the handoff

**Purpose:**
Make the hidden revenue leak concrete.

### Post 4
**File:** `blog/what-a-7-day-speed-to-lead-sprint-actually-fixes.html`

**Working title:**
What a 7-day speed-to-lead sprint actually fixes

**Purpose:**
Reduce ambiguity around the offer and support conversion.

---

## Implementation Tasks

### Task 1: Freeze phase 2 scope and article list

**Objective:** Lock the exact files and deliverables before rewriting content.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/docs/plans/2026-03-31-animas-phase-2-proof-and-blog-plan.md`

**Step 1: Confirm the case studies page remains in scope**
Expected outcome: `case-studies.html` will be fully rewritten.

**Step 2: Confirm the blog index is a curation layer**
Expected outcome: old posts stay live but come off the main grid.

**Step 3: Confirm the first 4 new articles**
Expected outcome: the four filenames in this plan are final unless Tyler changes them.

**Step 4: Commit planning updates if needed**
```bash
git add docs/plans/2026-03-31-animas-phase-2-proof-and-blog-plan.md
git commit -m "docs: finalize phase 2 proof and blog plan"
```

### Task 2: Rewrite case studies page metadata and hero

**Objective:** Reposition the page around consulting-firm workflow proof instead of generic AI automation wins.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/case-studies.html`

**Step 1: Replace page title, meta description, and OG tags**
Target ideas:
- "Case Studies | Workflow Wins for Consulting Firms"
- "See how Animas AI redesigns messy workflows, starting with urgent revenue-adjacent bottlenecks."

**Step 2: Replace hero headline and intro**
Target message:
- real workflow fixes
- one urgent bottleneck first
- proof of system design ownership

**Step 3: Verify page tone matches phase 1**
Expected: no broad agency language, no flat-rate retainer framing.

**Step 4: Commit**
```bash
git add case-studies.html
git commit -m "feat: rewrite case studies page framing"
```

### Task 3: Rewrite the Brander Group case study block

**Objective:** Build the anchor case study around a real client and Tyler's workflow ownership.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/case-studies.html`

**Step 1: Replace current challenge copy**
Write challenge in business terms, not tool terms.

**Step 2: Replace current solution copy**
Emphasize workflow mapping, system design, and implementation ownership.

**Step 3: Replace metrics/sidebar with placeholder-but-plausible claims Tyler can truth-correct**
Do not fabricate absurd nonsense. Keep claims adjustable and grounded.

**Step 4: Add bullets focused on operational result**
Examples:
- reduced manual handling
- faster execution
- clearer data flow
- more consistent internal process

**Step 5: Commit**
```bash
git add case-studies.html
git commit -m "feat: rewrite brander group case study"
```

### Task 4: Add two new strategic case study blocks

**Objective:** Make the case studies page support the new wedge and the expansion path.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/case-studies.html`

**Step 1: Replace the current lead qualification block with a stronger speed-to-lead case**
Message: faster follow up, cleaner intake, better routing, fewer dropped opportunities.

**Step 2: Replace the current SEO engine block with an adjacent-workflow expansion case**
Message: once first workflow wins, expand into onboarding/reporting/internal handoffs.

**Step 3: Keep design shell if useful, but align every headline and metric to current GTM story**

**Step 4: Commit**
```bash
git add case-studies.html
git commit -m "feat: add wedge-aligned case studies"
```

### Task 5: Rewrite final CTA and footer consistency on case studies page

**Objective:** Make the page end on the current conversion path.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/case-studies.html`

**Step 1: Replace final CTA copy with workflow-audit language**
Expected CTA: `Book a Workflow Audit`

**Step 2: Align supporting text with phase 1 pages**
Expected: no "implementation strategy" or generic automation CTA drift.

**Step 3: Update footer blurb if needed**
Expected: same consulting-firm workflow language used elsewhere.

**Step 4: Commit**
```bash
git add case-studies.html
git commit -m "chore: align case studies CTA and footer"
```

### Task 6: Rewrite blog index metadata and hero

**Objective:** Turn the blog landing page into a curated supporting asset for the new strategy.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/index.html`

**Step 1: Replace title, meta description, and OG tags**
Target message: workflow design, lead handling, consulting-firm operational bottlenecks.

**Step 2: Replace hero headline and intro**
Suggested direction:
- practical writing for founder-led consulting firms
- lead handling, onboarding, communication, and operational drag

**Step 3: Keep current structural shell**
Do not redesign. Just rewrite and curate.

**Step 4: Commit**
```bash
git add blog/index.html
git commit -m "feat: rewrite blog index framing"
```

### Task 7: Remove legacy posts from the blog landing grid without deleting their files

**Objective:** Keep old URLs live while cleaning the visible blog experience.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/index.html`

**Step 1: Remove the current legacy cards from the `BLOG_LIST_START` / `BLOG_LIST_END` section**
Remove only the cards, not the actual article files.

**Step 2: Keep legacy files untouched on disk**
Verification command:
```bash
python3 - <<'PY'
from pathlib import Path
files = [
    'blog/hotel-win-channel-intro.html',
    'blog/ai-agents-hospitality-future.html',
    'blog/openclaw-for-hotel-owners.html',
    'blog/openclaw-cloud-architecture.html',
    'blog/openclaw-google-workspace-setup.html',
]
for f in files:
    print(f, Path(f).exists())
PY
```
Expected: all print `True`

**Step 3: Commit**
```bash
git add blog/index.html
git commit -m "chore: remove legacy posts from blog landing grid"
```

### Task 8: Create the first new blog article

**Objective:** Publish the strongest thesis article tied to the wedge.

**Files:**
- Create: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/lead-handling-vs-lead-generation.html`
- Reference: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/template.html`

**Step 1: Copy article shell structure from an existing blog page or template**
Expected: preserve site styling and nav/footer consistency.

**Step 2: Write article metadata and hero**
Target headline: `Most consulting firms do not have a lead gen problem. They have a lead handling problem.`

**Step 3: Write body sections**
Suggested section headings:
- Why firms misdiagnose the problem
- Where leads actually get lost
- Why founder-led firms feel this pain harder
- What a better workflow changes
- What to do next

**Step 4: Add final CTA back to workflow audit**

**Step 5: Commit**
```bash
git add blog/lead-handling-vs-lead-generation.html
git commit -m "feat: add lead handling vs lead generation article"
```

### Task 9: Create the second new blog article

**Objective:** Support the main offer with a practical article.

**Files:**
- Create: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/what-a-7-day-speed-to-lead-sprint-actually-fixes.html`

**Step 1: Write metadata and hero**
**Step 2: Write sections explaining the sprint scope**
Suggested structure:
- what breaks before the sprint
- what gets audited
- what gets designed
- what gets implemented
- what comes next after the sprint

**Step 3: Add final CTA**

**Step 4: Commit**
```bash
git add blog/what-a-7-day-speed-to-lead-sprint-actually-fixes.html
git commit -m "feat: add speed-to-lead sprint explainer article"
```

### Task 10: Create the third new blog article

**Objective:** Make the hidden handoff problem concrete.

**Files:**
- Create: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/how-founder-led-firms-lose-leads-in-the-handoff.html`

**Step 1: Write metadata and hero**
**Step 2: Build article around recognizable failure points**
Suggested sections:
- delayed first response
- incomplete intake
- routing ambiguity
- follow-up inconsistency
- quiet revenue leaks

**Step 3: Add final CTA**

**Step 4: Commit**
```bash
git add blog/how-founder-led-firms-lose-leads-in-the-handoff.html
git commit -m "feat: add lead handoff failure article"
```

### Task 11: Create the fourth new blog article

**Objective:** Add a broader strategic article that still matches the ICP.

**Files:**
- Create: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/speed-to-lead-consulting-firms.html`

**Step 1: Write metadata and hero**
**Step 2: Write sections on why speed to lead matters for consulting firms**
Suggested sections:
- why service firms lose deals to process, not demand
- the founder bottleneck problem
- why speed creates trust before the sales call
- why one workflow win matters more than broad automation promises

**Step 3: Add final CTA**

**Step 4: Commit**
```bash
git add blog/speed-to-lead-consulting-firms.html
git commit -m "feat: add speed to lead consulting firms article"
```

### Task 12: Add the new posts to the blog landing page grid

**Objective:** Make the blog index show only the new aligned content.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/index.html`

**Step 1: Add four new blog cards inside the existing grid structure**

**Step 2: Order them intentionally**
Recommended order:
1. lead handling vs lead generation
2. what a 7-day sprint actually fixes
3. how founder-led firms lose leads in the handoff
4. why speed to lead matters more than firms think

**Step 3: Update CTA section copy if needed**
Make it flow back to the workflow audit.

**Step 4: Commit**
```bash
git add blog/index.html
git commit -m "feat: feature new consulting workflow articles on blog index"
```

### Task 13: Run a sitewide phase 2 consistency pass

**Objective:** Catch dumb drift before shipping.

**Files:**
- Modify if needed: `case-studies.html`
- Modify if needed: `blog/index.html`
- Modify if needed: `blog/*.html`

**Step 1: Search for old off-strategy phrases**
Run:
```bash
python3 - <<'PY'
from pathlib import Path
import re
root = Path('.')
terms = [
    'OpenClaw',
    'SMBs',
    'Agents as a Service',
    'flat-rate',
    'unlimited',
    'AI automation agency',
]
for path in list(root.glob('case-studies.html')) + list(root.glob('blog/*.html')):
    text = path.read_text()
    hits = [t for t in terms if t in text]
    if hits:
        print(path, hits)
PY
```
Expected: legacy posts may still contain old terms. New featured assets should not.

**Step 2: Search for em dashes in the new phase 2 assets only**
Run:
```bash
python3 - <<'PY'
from pathlib import Path
paths = [
    Path('case-studies.html'),
    Path('blog/index.html'),
    Path('blog/speed-to-lead-consulting-firms.html'),
    Path('blog/lead-handling-vs-lead-generation.html'),
    Path('blog/how-founder-led-firms-lose-leads-in-the-handoff.html'),
    Path('blog/what-a-7-day-speed-to-lead-sprint-actually-fixes.html'),
]
for p in paths:
    if '—' in p.read_text():
        print('EM DASH FOUND:', p)
PY
```
Expected: no output

**Step 3: Commit cleanup if needed**
```bash
git add case-studies.html blog/index.html blog/*.html
git commit -m "chore: align phase 2 proof and blog copy"
```

### Task 14: Verify locally and then push

**Objective:** Confirm all new assets render and the legacy posts still resolve.

**Files:**
- Verify all changed phase 2 files

**Step 1: Run a local static server**
```bash
python3 -m http.server 8787
```

**Step 2: Manually verify these paths**
- `/case-studies.html`
- `/blog/`
- `/blog/lead-handling-vs-lead-generation.html`
- `/blog/what-a-7-day-speed-to-lead-sprint-actually-fixes.html`
- `/blog/how-founder-led-firms-lose-leads-in-the-handoff.html`
- `/blog/speed-to-lead-consulting-firms.html`
- one legacy article URL such as `/blog/openclaw-for-hotel-owners.html`

**Step 3: Push**
```bash
git push origin master
```

**Step 4: Verify live site after Netlify updates**
Expected: case studies and blog reflect the new strategy, legacy posts still load directly.

---

## Content Quality Checklist

Before shipping phase 2, confirm:
- [ ] Brander Group is included
- [ ] Case studies page supports the speed-to-lead wedge
- [ ] Blog index shows only aligned articles
- [ ] Legacy hotel/OpenClaw posts still exist at their URLs
- [ ] New blog articles all point back to the workflow audit CTA
- [ ] No em dashes in the new featured assets
- [ ] No broad AI-agency language in the new featured assets
- [ ] Metadata matches the new consulting-firm positioning

---

## Recommended Execution Order

1. Rewrite `case-studies.html` framing and metadata
2. Rewrite Brander Group block
3. Rewrite remaining case study blocks
4. Rewrite `blog/index.html` hero and framing
5. Remove old cards from main blog grid
6. Create 4 new blog articles
7. Add new cards to blog grid
8. Run consistency checks
9. Verify locally
10. Push and verify deploy

---

## Definition of Done

Phase 2 is done when:
- `case-studies.html` reads like proof for the current GTM strategy
- Brander Group is presented as a real anchor case
- the blog landing page supports the consulting-firm speed-to-lead story
- legacy hotel and OpenClaw posts remain live but are no longer featured on the main blog page
- the new featured blog posts support the site's current wedge instead of distracting from it
- all featured phase 2 assets drive visitors back to the workflow audit CTA
