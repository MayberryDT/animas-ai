# Animas AI Speed-to-Lead Website Repositioning Plan

> For Hermes: use this plan to rewrite the existing static site around the current Animas AI manifesto and short-term GTM wedge.

**Goal:** Reposition the current website from a broad AI automation agency site into a focused conversion site for the 7-Day Speed to Lead Sprint aimed at founder-led B2B consulting firms.

**Architecture:** Keep the current static multi-page HTML structure and much of the visual system, but replace the current broad “agents as a service” and OpenClaw-heavy messaging with a tighter wedge-led narrative. Use the homepage as the primary sales page, keep secondary pages lean and supportive, and demote or remove off-strategy messaging that targets SMBs broadly, hotels, content automation, or unlimited-retainer language.

**Tech Stack:** Static HTML files with Tailwind via CDN, shared nav/footer patterns, embedded YouTube/video, hardcoded metadata.

---

## Current Site Assessment

### What is structurally usable
- Shared top nav and footer across pages
- Strong visual hierarchy on the homepage
- Reusable CTA button pattern
- Reusable card/grid sections
- Existing case study page shell
- Existing how-it-works page shell
- Existing static deployment setup via Netlify

### What is strategically off
- Homepage headline is broad and generic
- Metadata still sells “AI automation agency” and “SMBs” broadly
- Core narrative is “flat monthly retainer / unlimited requests” instead of the speed-to-lead wedge
- Repeated OpenClaw references expose implementation detail instead of client outcome
- Solutions page is service soup
- Blog is still heavily hotel/OpenClaw oriented and weakens ICP clarity
- Case studies are mixed and not tightly tied to consulting-firm lead handling
- CTA language changes too much across pages

### What to preserve
- Design system, spacing, typography, and button styling
- 7-day speed signal, but recast as the sprint offer
- Founder credibility section, but rewrite positioning around system design ownership
- One proof/case-study section if it can support the new wedge

### What to remove or demote
- “Agents as a Service” language
- “One Flat Monthly Rate. No Limits.” homepage framing
- “Powered by the OpenClaw Framework” sitewide callouts
- Content-autopilot and broad custom-ops cards as primary homepage messaging
- Hotel/OpenClaw blog content from primary navigation path if possible
- “Apply for Partnership” language unless it is intentionally the chosen CTA

---

## Target Information Architecture

### Homepage: `index.html`
Purpose: primary conversion page for the speed-to-lead wedge.

Target sections:
1. Hero
2. Problem section: lead handling, not lead gen
3. Outcome section: what the workflow changes
4. 7-Day Speed to Lead Sprint offer
5. How it works
6. Why Animas AI / Why Tyler
7. Brief expansion section for adjacent workflow work
8. Case study or proof strip
9. Final CTA

### Offer / Process Page: `how-it-works.html`
Purpose: explain the sprint process and reduce buying friction.

Target sections:
1. Hero focused on the sprint process
2. Who this is for
3. Step-by-step sprint flow
4. What is included
5. What happens after the sprint
6. FAQ
7. CTA

### Solutions Page: `solutions.html`
Purpose: secondary page showing adjacent workflow expansion after the first win.

Target sections:
1. Hero that starts with speed to lead
2. Secondary workflow areas
   - proposal and onboarding
   - reporting and client communication
   - internal handoffs and recurring ops
3. Why start with one workflow first
4. CTA back to audit or sprint

### Case Studies Page: `case-studies.html`
Purpose: proof page.

Target sections:
1. Hero focused on operational and revenue impact
2. Keep only studies that help the wedge narrative
3. If current studies stay, rewrite them to emphasize workflow ownership, time saved, and process outcomes
4. Add an explicit note that Animas starts with one urgent workflow, proves value, then expands
5. CTA

### Blog: `blog/index.html` and `blog/*.html`
Purpose: supporting authority only.

Recommended action:
- Keep blog accessible, but do not let it dominate nav strategy or ICP perception
- Review titles/descriptions for hotel/OpenClaw drift
- Consider a future content refresh toward consulting-firm workflow topics

---

## File-Level Implementation Tasks

### Task 1: Rewrite homepage metadata and hero

**Objective:** Make the homepage immediately communicate the new ICP, problem, and offer.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/index.html`

**Changes:**
- Replace `<title>` and meta description
- Replace Open Graph title/description
- Rewrite hero headline, subheadline, CTA labels
- Remove “AI automation agency,” “Agents as a Service,” and broad SMB language

**Verification:**
- Hero states who the site is for
- Hero states the business problem
- Hero states the 7-day offer
- CTA is consistent with chosen conversion path

### Task 2: Replace homepage pipeline banner with problem-first section

**Objective:** Shift the page from process theater to pain recognition.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/index.html`

**Changes:**
- Remove or heavily rework the “Our Proven Pipeline” strip
- Add problem section explaining lead handling vs lead generation
- Add revenue leak framing

**Verification:**
- Visitor can identify the exact problem being solved within the first two sections

### Task 3: Replace flat-rate retainer section with the sprint offer

**Objective:** Make the homepage sell the 7-Day Speed to Lead Sprint, not an unlimited retainer.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/index.html`

**Changes:**
- Remove “One Flat Monthly Rate. No Limits.”
- Replace “Zero API Fees” and “Fully Managed” cards with sprint-inclusion cards
- Rewrite guarantee language so it supports the sprint, not generic delivery bravado

**Verification:**
- Homepage clearly presents the front-end offer as the sprint
- Secondary retainer expansion is mentioned only after the initial offer is clear

### Task 4: Replace broad solution cards with wedge-aligned outcome blocks

**Objective:** Stop selling ten things at once.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/index.html`
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/solutions.html`

**Changes:**
- Remove homepage cards for content automation and broad ops as primary offers
- Add outcome blocks for faster follow up, cleaner intake, better routing, fewer dropped opportunities
- Reframe `solutions.html` around what comes after speed to lead

**Verification:**
- Homepage has one primary wedge
- Solutions page reads as expansion, not a random menu

### Task 5: Rewrite founder credibility section

**Objective:** Position Tyler as the system architect and implementation owner.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/index.html`

**Changes:**
- Keep headshot section shell
- Replace “Built by Master Craftsmen” language
- Emphasize that clients bring the outcome, Animas owns workflow design and implementation

**Verification:**
- Section screens out bad-fit clients who want a commodity implementer
- Section reinforces expertise without sounding inflated

### Task 6: Rewrite `how-it-works.html` around the sprint

**Objective:** Make the process page actually support the new offer.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/how-it-works.html`

**Changes:**
- Rewrite metadata
- Replace flat-rate retainer and unlimited-requests language
- Rewrite 5-step process into a sprint flow:
  1. audit current lead handling
  2. identify delays and gaps
  3. design the workflow
  4. implement core automation
  5. define next expansion path
- Replace OpenClaw references with client-facing workflow language

**Verification:**
- Page reduces friction for buying the sprint
- Process matches the manifesto and homepage messaging

### Task 7: Rewrite `solutions.html` as an expansion page

**Objective:** Make the solutions page support, not distract from, the wedge.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/solutions.html`

**Changes:**
- Rewrite hero around workflow systems for consulting firms
- Replace current solution grid with 3 adjacent workflow areas
- Add section explaining why Animas starts with one urgent workflow first

**Verification:**
- Page no longer reads like broad agency services
- Secondary services are clearly downstream of the first workflow win

### Task 8: Tighten `case-studies.html`

**Objective:** Keep proof, remove drift.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/case-studies.html`

**Changes:**
- Rewrite hero to align with the new wedge
- Audit each case study for fit with consulting-firm workflow automation
- Keep only proof that helps the new narrative or rewrite framing to support “one workflow first, then expand”

**Verification:**
- Proof page supports the homepage story instead of opening new categories

### Task 9: Audit navigation, CTA consistency, and metadata sitewide

**Objective:** Eliminate message drift.

**Files:**
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/index.html`
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/how-it-works.html`
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/solutions.html`
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/case-studies.html`
- Modify: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/index.html`

**Changes:**
- Standardize CTA labels
- Remove “Apply for Partnership” unless intentionally retained everywhere
- Update titles, descriptions, and OG copy to match the new positioning
- Remove OpenClaw callouts from buyer-facing pages unless strategically necessary

**Verification:**
- All pages use the same primary story
- No page reintroduces the old broad-agency framing

### Task 10: Decide what to do with the blog and hotel content

**Objective:** Prevent supporting content from confusing ICP.

**Files:**
- Review: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/index.html`
- Review: `/home/nova/.openclaw/workspace/animas-ai-site-20260331/blog/*.html`

**Decision options:**
1. Keep blog in nav, but accept current drift temporarily
2. Keep blog live but remove from primary nav
3. Keep nav link but rewrite blog index intro so it is clearly supporting content
4. Later, replace hotel/OpenClaw content with consulting-firm workflow content

**Verification:**
- The main conversion path still feels built for founder-led consulting firms

---

## Recommended Order of Execution

1. Rewrite `index.html`
2. Rewrite `how-it-works.html`
3. Rewrite `solutions.html`
4. Tighten `case-studies.html`
5. Audit nav, CTA consistency, and metadata
6. Decide blog/nav treatment
7. Preview pages locally and verify copy hierarchy
8. Commit and deploy

---

## Keep / Change / Remove Summary

### Keep
- Static HTML approach
- Visual style and layout system
- Existing nav/footer scaffolding
- Founder credibility section shell
- Case-study page shell

### Change
- Homepage narrative
- Page metadata
- CTA wording
- Process framing
- Solutions framing
- Case-study framing

### Remove or demote
- Broad SMB messaging
- Unlimited retainer positioning as the homepage lead
- OpenClaw as a buyer-facing trust badge
- Hotel/open-source/tool-first positioning in the main funnel
- Broad service menu thinking

---

## Definition of Done

The repositioning is done when:
- the homepage clearly targets founder-led consulting firms
- the site clearly frames the problem as lead handling, not lead generation
- the 7-Day Speed to Lead Sprint is the primary offer everywhere that matters
- Tyler is positioned as the expert who owns workflow design and implementation end to end
- broader automation work appears only as a secondary expansion path
- sitewide metadata and CTA language stop contradicting the strategy
