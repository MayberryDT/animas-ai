# Animas AI Legion Tools Website Integration Plan

> **For Hermes:** Use this plan to bring the completed wedge tools from Halla into the public Animas AI website cleanly, without dragging in drift or breaking the current speed-to-lead positioning.

**Goal:** Integrate the completed top-of-funnel tools built by Mark and Veego on Halla into the Animas AI website so they can be used as on-site conversion assets and linked in the outbound email sequence that Gunny is now ready to run.

**Architecture:** The tools already exist on Halla as self-contained static HTML apps. The Animas AI website is also a static multi-page HTML site. The cleanest implementation path is to import each completed tool as its own standalone page under the website repo, align shared nav/footer/copyright/CTA copy with the current site, add a dedicated tools section to the public website, and then wire the homepage, blog, outbound links, and CTA surfaces to those pages.

**Tech Stack:** Static HTML + Tailwind via CDN + Google Fonts (Manrope / Inter). No backend required for initial integration. Current public site repo: `/home/nova/.openclaw/workspace/animas-ai-site-20260331`.

---

## What I found on Halla

### Completed tool builds
Located on Halla under `/home/halla/creations/`:

1. `/home/halla/creations/lead-response-time-calculator/`
2. `/home/halla/creations/intake-form-teardown/`
3. `/home/halla/creations/speed-to-lead-audit/`
4. `/home/halla/creations/lead-handoff-scorecard/`

Each directory contains:
- `index.html`
- `prd.json`
- `status.json`
- `current-task.md`
- `result.md`

### Build status
These are not rough stubs. They read as completed loops.

- **Lead Response Time Calculator**
  - `status.json`: `US-010 PASS - Final Polish + QA`
- **Intake Form Teardown**
  - `status.json`: `PASS`
- **Speed-to-Lead Audit**
  - `status.json`: `PASS`
- **Lead Handoff Scorecard**
  - `status.json`: `US-011 PASS — Final Polish + QA. Loop complete.`

### What they are
Based on the PRDs and completion notes:
- all four are **self-contained static HTML tools**
- all four match the current visual direction: white/light backgrounds, slate text, blue/indigo accents, Manrope + Inter, rounded cards, soft shadows
- they are explicitly designed as **wedge tools** for the Animas AI GTM system
- they are intended to bridge toward:
  - the website
  - the email sequence
  - the 7-Day Speed to Lead Sprint

### Tool ladder confirmed
From existing local notes and briefs:
1. Lead Response Time Calculator
2. Intake Form Teardown
3. Speed-to-Lead Audit
4. Lead Handoff Scorecard

This matches the outbound email sequence logic already written in local notes.

### New relevant runtime update
Gunny is now configured and ready on Halla with a fixed 4-email sequence and explicit tool mentions.

Confirmed sequence mapping:
- Email 1 → Lead Response Time Calculator
- Email 2 → Intake Form Teardown
- Email 3 → Speed-to-Lead Audit
- Email 4 → Lead Handoff Scorecard

Implication:
The website should not treat these tools as optional side assets anymore. They now sit directly inside the outbound system, so public page paths, CTA destinations, and on-site tool naming need to be stable enough for Gunny to reference without ambiguity.

---

## What this means
The real work is **not inventing the tools**. That part is done.

The real work is:
1. importing them into the public website repo
2. normalizing shared copy/UI details so they feel like one site, not four foreign bodies
3. wiring the website and email sequence around them intentionally

That is manageable.

---

## Recommended integration approach

### Preferred path
Import each tool as a dedicated public page in the Animas AI website repo.

Suggested target paths:
- `/lead-response-time-calculator.html`
- `/intake-form-teardown.html`
- `/speed-to-lead-audit.html`
- `/lead-handoff-scorecard.html`

Why this path holds:
- the main site is already static HTML
- the tools are already static HTML
- no framework migration needed
- easiest way to preserve tool polish and ship fast
- easy to link from email, blog, homepage, and case studies

### Avoid for now
- embedding each tool directly inside the homepage
- rebuilding them in a different framework first
- adding backend or auth
- over-abstracting shared components before first integration works

That would be a choice. Not the good one.

---

## Integration tasks

### Task 1: Pull the built tool files off Halla

**Objective:** Bring the four completed tool pages into the website repo for review and integration.

**Source files on Halla:**
- `/home/halla/creations/lead-response-time-calculator/index.html`
- `/home/halla/creations/intake-form-teardown/index.html`
- `/home/halla/creations/speed-to-lead-audit/index.html`
- `/home/halla/creations/lead-handoff-scorecard/index.html`

**Target files in website repo:**
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/lead-response-time-calculator.html`
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/intake-form-teardown.html`
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/speed-to-lead-audit.html`
- `/home/nova/.openclaw/workspace/animas-ai-site-20260331/lead-handoff-scorecard.html`

**Verification:**
- all four files render locally
- no copy is obviously stale or off-strategy
- no broken external asset references

### Task 2: Normalize sitewide shell and CTA behavior

**Objective:** Make imported tools feel native to Animas AI, not separate artifacts.

**Files:**
- the four imported tool HTML files

**Required edits:**
- use current nav structure
- use current footer structure
- normalize copyright year to 2026
- normalize CTA language to current preferred CTA
- remove any stale or inconsistent copy drift
- ensure no em dashes in customer-facing copy if present

**Verification:**
- each tool page visually matches the rest of the site
- nav links behave like the core site
- footer and CTA language feel consistent

### Task 3: Review each tool against current website positioning

**Objective:** Confirm the tool copy still matches the current wedge and not an older variant.

**Checks per tool:**
- is it clearly for founder-led consulting firms?
- does it reinforce lead handling, not lead gen?
- does it point toward the Speed-to-Lead Audit or Sprint appropriately?
- does it sound operational, not fluffy?
- does it avoid generic AI-agency language?

**Likely outcomes:**
- **Speed-to-Lead Audit** should probably remain the flagship diagnostic
- **Lead Response Time Calculator** and **Lead Handoff Scorecard** should remain supporting wedge tools
- **Intake Form Teardown** should be reviewed carefully to ensure its CTA path is consistent with the website hierarchy

### Task 4: Decide the on-site tool hierarchy

**Objective:** Prevent four tools from competing equally and confusing visitors.

**Recommended hierarchy:**
- **Primary website tool:** Speed-to-Lead Audit
- **Secondary tools:**
  - Lead Response Time Calculator
  - Lead Handoff Scorecard
  - Intake Form Teardown

**Recommendation:**
- homepage should still primarily push **Book a Workflow Audit**
- the site can optionally reference the **Speed-to-Lead Audit** as the main self-serve diagnostic
- the other tools should live on the site and be used more heavily in email and content than in top-nav prominence

### Task 5: Wire tools into the current blog and outbound ecosystem

**Objective:** Make the tools usable from the email sequence and blog posts.

**Integration points:**
- relevant blog posts should link to the matching tool
- email sequence should map one email to one tool, as already documented
- tool result screens should route to the audit or sprint depending on the tool’s job

**Current mapped sequence from notes:**
- Email 1 → Lead Response Time Calculator
- Email 2 → Intake Form Teardown
- Email 3 → Speed-to-Lead Audit
- Email 4 → Lead Handoff Scorecard

**Verification:**
- every tool has a clear role in the sequence
- no tool exists as an orphaned page with no distribution path

### Task 6: Add a dedicated tools section to the website

**Objective:** Make the tool ladder visible on the public site in one clear place so visitors and Gunny's outbound links both have a stable home base.

**Recommended placement:**
- add a dedicated **Tools** section on `solutions.html`

**Recommended contents:**
- Lead Response Time Calculator
- Intake Form Teardown
- Speed-to-Lead Audit
- Lead Handoff Scorecard

**Rules:**
- keep the section customer-facing
- explain what each tool helps diagnose
- do not make all four compete equally with the main service offer
- keep Speed-to-Lead Audit framed as the flagship diagnostic
- once the imported tool pages exist, the cards should link to their stable public paths

### Task 7: Add internal linking on the website where useful

**Objective:** Use the tools without cluttering the main site.

**Suggested placements:**
- homepage: optional supporting mention of the flagship diagnostic only
- tools section: stable list of all four tools
- blog posts: direct contextual links to matching tools
- case studies: optional “diagnose your own process” CTA
- footer: no need to add all four tools unless that proves useful later

### Task 8: Local verification and deployment check

**Objective:** Make sure imported tools actually work inside the website repo.

**Verification checklist:**
- pages load without console errors
- mobile layout still holds
- all links work
- shared fonts and Tailwind load
- results sections and calculators still function after import
- copy and footer are normalized

---

## Risk notes

### Main risk
The tools may be visually polished but still contain:
- stale CTA text
- old footer year
- inconsistent copy style
- old phrasing from before the latest site tightening

That is fixable. It just needs a disciplined pass.

### Secondary risk
If all four tools are featured equally on the public site, the message will sprawl again.

Do not do that.

One flagship tool. Supporting tools underneath.

### Low risk
Because these are static pages, integration should be mechanically straightforward.

This is not a platform rebuild. It is content and page import work.

---

## Recommended execution order

1. import the four Halla tool pages into the website repo
2. normalize nav/footer/CTA/copyright
3. review each tool’s copy against current positioning
4. declare one flagship tool and three supporting tools
5. add the dedicated website tools section
6. wire tool links into blog and email assets, with Gunny sequence paths in mind
7. test locally
8. push and verify deploy

---

## Definition of done

This integration is done when:
- all four tools exist inside the Animas AI website repo
- each one renders correctly from the public site
- CTA and footer language are consistent with the current website
- the tool hierarchy is clear, with Speed-to-Lead Audit as flagship
- blog and email sequence can link to the tools intentionally
- the site gains useful conversion assets without drifting back into service soup
