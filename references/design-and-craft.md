# Design and craft

Labels: [Saved] from saved reels; [Researched] checked against sources on 3 November 2026; [Practice] good practice; [Distilled] summarised from a companion skill (see [companion-skills.md](companion-skills.md)).

## The rule that overrides the rest

**The brand and the brief win.** Every "tell" below is a default to question, not a ban. If a project's brand file chose a serif, a cream background, a full stop after a name or italics, keep it. What matters is that each visible choice was made for this project, not reached for by habit. [Distilled from Impeccable]

## 1. Decide before building

- [ ] Name the subject, audience and main job of the page.
- [ ] Write one sentence as the design "north star", and make type, colour, imagery and motion serve it. [Distilled from Oil UI]
- [ ] Pick the mode from the surface, not the product [Distilled from Impeccable]:
  - **Persuade** (landing, pricing, campaigns): earn attention and action; bolder work is allowed.
  - **Operate** (app screens, dashboards, settings): scanability, consistency and familiar patterns beat expression.
  - **Read** (docs, articles, help, legal pages): structure for comprehension.
  - **Experience** (portfolio, gallery): the work leads and the interface recedes.
- [ ] Choose 4 to 6 named colours, 1 or 2 typefaces, a layout concept and a few principles.
- [ ] Ask: "Would this plan suit any similar page?" If so, change it.
- [ ] Use real content and real photos from the start.
- [ ] Spend boldness on one memorable element, and keep the rest quiet.
- [ ] Use a brand or design file on every screen, because a new page can otherwise drift back to defaults.

## 2. Keep a DESIGN.md in every project

A DESIGN.md is a plain markdown design system that any agent reads before building UI (the format comes from Google Stitch; [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) has 84 examples). If the project has none, write one before the first screen, from the brand. Typical sections:

1. Overview: the feel in two or three sentences
2. Colours: brand, surfaces, text and semantic colours (success, warning, danger, info), with hex values and roles
3. Typography: families, a size and weight scale, line heights, principles
4. Layout: spacing scale, grid, container widths, whitespace
5. Elevation and depth: shadows and surface steps
6. Shapes: radius scale
7. Components: buttons, inputs, cards, navigation, footer, with states
8. Do's and don'ts
9. Responsive behaviour: breakpoints, touch targets, how layouts collapse

Read it before every UI change. If code and DESIGN.md disagree, say so and ask which wins; never merge them silently. [Distilled from Oil UI]

## 3. Structure before style [Distilled from Oil UI]

- [ ] Give each screen one hero and one main action. Merge or demote anything competing with it.
- [ ] Sketch the main viewport in greyscale first: content order, main action and states. If the structure doesn't work in grey, colour and fonts won't save it.
- [ ] Build one representative page or the core flow with its key states, check it, then roll out.
- [ ] Use realistic content. Never fake customer reviews, results or metrics, and never leave "example" or "placeholder" text on screen.

## 4. Four patterns every app needs [Saved]

From the @haydenschmitty reel ("4 design patterns your vibe-coded app should be using").

1. **Skeleton loaders.** Grey bars in the shape of the layout while data loads. They cut perceived waiting time. Match the real content's geometry so nothing jumps.
2. **Semantic colours.** Besides the brand palette, define success, warning, danger and info, each with light to dark shades, and use them consistently. Not using them makes an app harder to read.
3. **Remove clutter.** AI tools love a two-sentence description under every heading ("My Day" does not need explaining). If it isn't tangibly useful, remove it.
4. **Accessibility.** The most common gap in vibe-coded apps, and one that can lead to complaints or legal action. Check against WCAG 2.2 AA (see [legal-and-compliance.md](legal-and-compliance.md)).

## 5. Tells that make a design look generated

### First wave [Researched]
- Purple or indigo fading to blue, including gradient headline text
- Inter, Geist or Roboto left as the default on everything
- Centred hero followed by three identical icon cards
- Identical rounded cards with the same soft grey shadow
- Emoji used as icons
- Glassmorphism, neon glow and 3D blobs
- Coloured left borders on cards
- Stock component library styling left untouched

### Second wave [Researched]
Asking for "less AI" often produces these instead:
- Warm cream background, high-contrast serif and terracotta accent
- Near-black background with one acid-green or vermilion accent
- Broadsheet layout with hairline rules and square corners

### Typography and structure [Researched]
- One accented word in a headline
- All-caps labels and an eyebrow above every heading
- Numbered markers such as 01, 02 and 03 when the content is not a sequence
- Meta strings joined with middle dots
- Monospace used for small labels as decoration
- An arrow added to every link or button
- Fade-and-slide animation on every section and hover effect on every card

### 20 AI design slop indicators [Saved]
From the @charles.unemployed reel.

| | | | |
|---|---|---|---|
| 1. Tags and pills | 6. Overusing dividers | 11. Code breadcrumbs | 16. Squircles |
| 2. Excessive italics | 7. Colour shades and opacities | 12. Section numbering | 17. Excessive mono fonts |
| 3. Instrument Serif | 8. Containers with borders | 13. Eyebrows | 18. ALL CAPS subtitles |
| 4. Negative kerning | 9. Overly detailed diagrams | 14. Dithering | 19. Gradient backgrounds |
| 5. Over-the-top detailed UI | 10. Verbose, redundant text | 15. ASCII images | 20. Periods in titles |

### Also refuse by default [Distilled from Impeccable]
- Same-size cards of icon, heading and text as the whole page structure; cards inside cards
- The hero-metric template: big number, small label, supporting stats
- A modal for a task that needs neither interruption nor protected focus
- Hard offset shadows (`4px 4px 0`) outside a genuinely neobrutalist brand
- Sparklines, progress rings and soft rounded boxes standing in for real content
- Unicode glyphs or emoji instead of one consistent icon set
- Light or dark chosen by category rather than by where and when people use it

### Better habits [Researched]
- [ ] Give the hero something specific to the subject, not a large stat with a gradient accent.
- [ ] Keep line lengths under 80 characters.
- [ ] Make the visual hierarchy show what matters most.
- [ ] Limit automatic motion to one deliberate moment, and respect reduced motion settings.
- [ ] Keep visible keyboard focus and make layouts work on mobile.

## 6. Worked example: the OTP screen [Saved]

From the @charles.unemployed "Removing AI slop" reel, starting from the verification screen AI tools produce:

1. Remove the purple gradients and auto-submit when the last digit is entered. "Now it feels trustworthy."
2. Cut the extra words and drop the borders.
3. Improve the contrast of the digit tiles. (The reel also adds an iridescent background: a style choice, not a rule.)
4. Animate typing and give each state visual feedback: checking, wrong code (shown on the tiles, with text, not colour alone), verified.
5. Autofill the code from the text message (`autocomplete="one-time-code"` on the web), so nobody has to type.

## 7. Craft floor: check on the rendered page [Distilled from Impeccable]

- [ ] **Contrast:** body and placeholder text at least 4.5:1, large text 3:1. On coloured surfaces, tint secondary text from that colour, not grey.
- [ ] **Depth:** shadows have an offset and a soft blur; a zero-offset coloured glow is decoration.
- [ ] **Spacing:** tight inside groups, generous between them, more space above a heading than below it.
- [ ] **Type:** body lines about 65 to 75 characters; clear steps in size and weight; balanced headings; real copy tested at every breakpoint.
- [ ] **Motion:** one deliberate moment, not the same entrance on every section (see [motion-and-faux-ui.md](motion-and-faux-ui.md)).
- [ ] **States:** hover, focus, disabled, loading, error and empty all designed.
- [ ] **Browser surfaces:** text selection colour, caret, scrollbars, focus rings, link underline offset and tabular numbers in data are themed, not left as defaults.
- [ ] **Copy:** controls name their action; errors name the problem and the fix.
- [ ] **Coverage:** every requirement in the brief is present and findable within seconds.

## 8. Copy [Researched]
- [ ] Cut empty words such as unlock, elevate and seamless.
- [ ] Never invent statistics, customers, logos or testimonials. This is also a legal risk.
- [ ] Say exactly what a button does: "Save changes", not "Submit".
- [ ] Keep the same word for an action throughout: "Publish" leads to "Published".
- [ ] Make errors explain what happened and how to fix it. They should not apologise or be vague.
- [ ] Make empty screens say what to do next.

## 9. Review what actually renders [Distilled from Oil UI and Impeccable]

- [ ] Look at screenshots at the sizes it ships at: desktop, about 390px and 360px phone widths, and 200% browser zoom.
- [ ] Judge "does it look right" and "does the task work" separately. Walk the main flow from its real entry point, save, reload and check it read back; force a failure and check the input was kept.
- [ ] Batch fixes, then look again, rather than screenshotting after every tweak.
- [ ] If a fresh reviewer (a subagent or a second model) is available, have it review the screenshots without seeing the code or the process.
- [ ] If screenshots aren't possible, say "visual result not verified" rather than claiming it looks right.
