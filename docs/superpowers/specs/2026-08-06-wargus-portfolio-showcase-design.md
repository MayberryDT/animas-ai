# Wargus TypeScript — Site Showcase Design (Approach B)

**Date:** 2026-08-06  
**Status:** Approved direction (Approach B)

## Goal

Add **Wargus TypeScript** as a new public product card on:

1. Animas AI homepage selected-work grid (`animasai.co` / repo `MayberryDT/animas-ai`)
2. Personal portfolio homepage (`tylermayberry.dev` / repo `MayberryDT/apps-portfolio`)

Use a **polished showcase image first** (Approach B), then ship the listings.

## Product facts (public-safe)

| Field | Value |
| --- | --- |
| Name | Wargus TypeScript |
| Live URL | https://wargus.animasai.co |
| One-liner | Browser-native TypeScript/PixiJS port of Wargus (Warcraft II–style RTS). Fixed Garden of War human-vs-AI demo: harvest, train, build, fight in the browser. |
| Positioning | Playable technical demo / creative systems build — not a commercial SaaS claim |
| Stack signal | TypeScript, PixiJS, Vite, browser-native RTS simulation |

## Scope

**In**

- Polished 16:9 (or near) showcase asset derived from real demo footage when possible
- Animas homepage card only
- Portfolio homepage new card (append only)
- Portfolio layout CSS so cards are not dumped into one flat row
- Portfolio copy “five” → current count; schema `ItemList` update
- Portfolio standing rule: new products = new cards; never remove unless asked

**Out**

- Animas case studies page
- Dedicated `/wargus.html` build-notes page
- Resume updates
- Product work inside the Wargus game repo
- Replacing any existing card

## Standing rule

When asked to add a product to the portfolio (or Animas work index), **always append a new card**. Never remove or replace an existing card unless the user explicitly says so.

## Visual direction

- Prefer a **real in-browser capture** of the Garden of War demo as the factual base (terrain, units, HUD).
- Polish into a portfolio-grade product frame (contrast, crop, subtle framing) without inventing fake UI chrome that misrepresents the product.
- Match existing card media: wide hero crop, readable at card size, dark RTS palette is fine.
- Reuse the same master asset (or lightly cropped variant) on both sites.

## Placement

### Animas AI (`index.html`)

- Homepage selected-work grid only
- Insert near other playable/demo work (adjacent to Rat Detective Online is natural)
- Visual treatment: dark card like Rat Detective (playable product)

### Portfolio (`apps-portfolio/index.html`)

- Append as sixth product card in supporting grid
- Keep Masthead as sole featured card
- Desktop supporting layout (not one row of five):

```
pip | executioner
rat (full width)
milk | wargus
```

- Mobile: single-column stack (existing pattern)

## Success criteria

- [ ] Showcase image exists in both repos and looks intentional at card size
- [ ] Animas homepage links to https://wargus.animasai.co and shows the card
- [ ] Portfolio homepage shows six products; no existing card removed
- [ ] Portfolio intro/schema copy no longer says “five” without Wargus
- [ ] Layout remains multi-row on desktop
- [ ] AGENTS.md (or equivalent) records append-only product rule
