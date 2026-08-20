---
version: alpha
name: Animas AI
description: A direct, engineered portfolio and studio site built around shipped proof.
colors:
  primary: "#020617"
  secondary: "#475569"
  tertiary: "#2563EB"
  neutral: "#EDF4F6"
  surface: "#FFFFFF"
  outline: "#1E3A8A"
  outline-subtle: "#E5E7EB"
  inverse: "#FFFFFF"
typography:
  display-xl:
    fontFamily: Manrope
    fontSize: 72px
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: -0.04em
  display-md:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.035em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.02em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.45
    letterSpacing: 0.1em
rounded:
  none: 0px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  section: 96px
  container: 1280px
components:
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
  hero-heading:
    textColor: "{colors.primary}"
    typography: "{typography.display-xl}"
  section-heading:
    textColor: "{colors.primary}"
    typography: "{typography.display-md}"
  project-section:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.section}"
  project-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  project-title:
    textColor: "{colors.primary}"
    typography: "{typography.headline-md}"
  project-meta:
    textColor: "{colors.tertiary}"
    typography: "{typography.label-caps}"
  body-copy:
    textColor: "{colors.secondary}"
    typography: "{typography.body-lg}"
  supporting-copy:
    textColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.inverse}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    height: 44px
    padding: "{spacing.md}"
  button-primary-hover:
    backgroundColor: "{colors.tertiary}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.outline}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    height: 44px
    padding: "{spacing.md}"
  navigation-link:
    textColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
  hairline:
    backgroundColor: "{colors.outline-subtle}"
    height: 1px
---

# Animas AI Design System

## Overview

Animas AI should feel like a working studio run by a capable builder: direct, precise, practical, and visibly grounded in shipped products. The site is not a generic AI consultancy landing page and not a decorative portfolio concept. Its job is to establish what Tyler builds, show credible proof quickly, explain the operating approach, and make contact easy.

The visual language combines editorial clarity with the discipline of an architectural drawing. Large Manrope headlines carry the personality; Inter keeps explanation readable; JetBrains Mono is reserved for useful product metadata and technical actions. The emotional target is confident and sophisticated without becoming sterile, corporate, or theatrical.

The homepage remains a complete studio narrative in this order: hero, services, shipped work, operating thesis, founder, and contact. Shipped work is the visual center of gravity, but it supplements rather than replaces the rest of the site. This design system applies to every Animas AI marketing page, product page, resume page, blog index, and blog article. Standalone application interfaces under `audit`, `calculator`, `intake`, and `scorecard` are separate products and do not inherit the marketing-site shell.

## Colors

The palette keeps the existing Animas AI identity: deep ink, cool slate, blueprint blue, pale blue-gray, and white.

- **Primary (`#020617`):** Headlines, primary text, dark actions, and the darkest page fields.
- **Secondary (`#475569`):** Body copy and supporting information.
- **Tertiary (`#2563EB`):** Interactive emphasis and useful technical metadata. Use it sparingly.
- **Neutral (`#EDF4F6`):** The default site canvas beneath every marketing, product, resume, and editorial page.
- **Surface (`#FFFFFF`):** Cards, navigation, and high-contrast content areas.
- **Outline (`#1E3A8A`):** Structural borders and rules in the shipped-work system.
- **Outline subtle (`#E5E7EB`):** Quiet dividers outside the shipped-work system.

Maintain WCAG AA contrast for text and controls. Blueprint blue is an accent, not a substitute for hierarchy; a heading should not need blue microcopy above it to make sense.

Gradients are prohibited. Every surface uses a single flat color. Create atmosphere and depth with line work, borders, spacing, opacity, imagery, and adjacent tonal fields instead of blended color transitions.

## Typography

Typography does most of the expressive work.

- **Manrope:** Display and card headlines. Use 700 or 800 weight, tight tracking, and compact line height.
- **Inter:** Navigation and explanatory copy. Keep paragraphs conversational and easy to scan.
- **JetBrains Mono:** Product category metadata and short action labels only. Set it uppercase with generous tracking.

Responsive display type should step down rather than wrap into awkward single-word lines. At narrow widths, the 72px hero display can reduce to 36px and the 48px section display can reduce to 30px. Keep visible headings plain and meaningful. Do not add an eyebrow, subtitle, or annotation when the headline already carries the message.

## Layout

Use a fixed-max-width desktop grid with a `1280px` content container and responsive outer gutters: 16px on mobile, 24px on small screens, and 32px on desktop. Major sections use approximately 96px of vertical padding, reducing on small screens only when necessary. Every included page loads the shared `/assets/animas-site.css` shell and identifies its page family on `<body>`. Page-specific HTML owns content and layout; the shared shell owns palette, background, shape, depth, navigation treatment, and editorial defaults.

The shipped-products grid follows the selected Architectural Cut Sheet direction:

- One column on mobile.
- Two equal columns from 768px through large tablet widths.
- Six underlying columns from 1280px upward. The first two flagship cards each span three columns; the remaining six cards each span two columns, producing a 2–3–3 arrangement.
- Use a 14px grid gap and keep every card aligned to the same structural rules.

The work-section header contains one headline, `A working set of shipped products.`, and may include the archive action aligned opposite it. It does not contain an eyebrow, descriptive paragraph, sheet number, or drawing-plane annotation.

## Elevation & Depth

Depth comes from tonal sections, strong borders, image fields, and whitespace—not from rounded floating panels. The default site canvas is a pale blue-gray field with dense, fine blue cyber linework behind white or ink content surfaces. Whitespace should reveal the canvas; reading and interaction surfaces should protect legibility with a flat, high-contrast fill.

Site-wide background linework is computer-native and non-geographic. Every background line uses one token: `#2563EB` at 8% opacity and 1px width. Keep every line the same color, darkness, and weight. Do not introduce major/minor hierarchy, darker accents, geographic contours, sea-chart shapes, square grids, checkerboards, hand-drawn waves, or color gradients.

The **Terminal Scan Paths** field (`/assets/animas-line-field-05.svg`) is the default Animas AI background across the entire included site: dense broken horizontal runs with measured gaps and small digital offsets. Treat it as a core brand surface, not an interchangeable section decoration. It remains static, non-animated, and subordinate to content. On long pages it may repeat vertically; on narrow screens it may crop rather than shrink into visual noise. The design-direction source remains under `docs/design/generated/`; the generator copies the selected production field into the publishable `assets/` tree.

Use shadows only when a functional layer must detach from the page, such as fixed navigation or an overlay. Keep those shadows quiet. New cards should rely on border and background contrast instead of ornamental drop shadows.

Project images start slightly desaturated and return to full color on hover. The transition should feel controlled and subtle. Respect `prefers-reduced-motion` by removing nonessential movement.

## Shapes

The shape language is architectural and rectilinear. Cards, buttons, images, inputs, navigation controls, and content panels use `0px` corner radius. Use straight 1px or 2px rules to define containment and hierarchy. Pill-shaped controls, tags, and badges are prohibited.

Icons may retain their native internal geometry, but their surrounding control stays square. Circular badges, pills, capsules, and rounded cards are outside this system unless the underlying content is literally circular, such as a portrait crop or radial data visualization.

## Components

### Navigation

Use a translucent white fixed bar with a subtle bottom rule. The wordmark stays compact. Desktop navigation uses quiet slate links; the contact action is a sharp dark rectangle. Mobile navigation must expose the same destinations and preserve keyboard access.

### Buttons and Links

Primary buttons use the primary ink field with white text, square corners, compact padding, and an explicit hover shift to tertiary blue. Secondary actions use white or transparent fields with a visible structural border. Labels should describe the destination or action directly. Arrow icons may move a few pixels on hover, but the control itself should remain visually stable.

### Project Cards

Every shipped-product card includes one proof image, one useful metadata line, a product title, a concise outcome-oriented description, and a destination. Cards use white surfaces, 2px outline borders, and no corner radius. Do not number the cards. Project metadata may be blue because it communicates category and release state; decorative blue labels around the section heading are not part of the component.

Images use a consistent 16:9 field with `object-fit: cover`. Copy areas use consistent padding and a minimum height sufficient to align actions. The action sits at the bottom of the copy area behind a 1px rule.

### Service and Thesis Cards

These cards remain quieter than project cards. Use white surfaces, subtle borders, square corners, concise copy, and one clear icon. They support the portfolio rather than compete with it.

### Product and Marketing Pages

Heroes sit on white cut-sheet panels with 2px navy structural borders. Proof imagery, system explanations, feature cards, and calls to action use the same rectilinear surface language as the homepage. Product-specific teal, amber, rose, or decorative color themes are not retained; category differences come from copy, imagery, and layout while interaction emphasis remains blueprint blue.

### Blog Index and Articles

The blog index uses square white editorial cards with navy rules and blue metadata. Blog articles use a centered white reading sheet above the Terminal Scan Paths canvas. Article headings remain Manrope, long-form prose remains Inter, and code or technical metadata may use JetBrains Mono. Blockquotes, tables, author panels, and article calls to action use straight structural borders. The blog template must inherit the same shell so future posts conform by default.

### Section Headers

Prefer one strong headline. Add supporting copy only when it supplies information the headline cannot. A section label is appropriate only when it improves navigation or meaning; it is not a default decoration. The shipped-work header is intentionally limited to its headline and archive action.

## Do's and Don'ts

- Do lead with shipped proof and working destinations.
- Do preserve the full homepage narrative around the portfolio section.
- Do use square geometry, strong alignment, and visible structural rules.
- Do reserve blue monospaced text for useful project metadata and technical actions.
- Do write short, concrete copy that says what was built or why it matters.
- Do keep responsive behavior intentional at mobile, tablet, and desktop widths.
- Do expose the Terminal Scan Paths canvas in page whitespace while protecting long-form reading with white surfaces.
- Do use one shared site shell for all marketing, product, resume, and blog pages.
- Don't add card numbers, sheet identifiers, faux drafting notes, or ornamental annotations.
- Don't add an eyebrow or subtitle when the section headline is already self-explanatory.
- Don't reintroduce rounded corners, pill buttons, or capsule tags.
- Don't use gradients in backgrounds, buttons, overlays, text, illustrations, or decorative effects.
- Don't introduce page-specific accent palettes that compete with the ink, slate, blueprint-blue, navy, pale blue-gray, and white system.
- Don't apply the marketing-site shell to the standalone `audit`, `calculator`, `intake`, or `scorecard` application interfaces.
- Don't replace the hero, services, thesis, founder, or contact sections with a portfolio-only page.
- Don't use AI-industry slogans where specific proof can carry the message.
