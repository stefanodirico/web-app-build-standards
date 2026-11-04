# Companion skills and design references

These are other people's open-source skills. This standard keeps their key ideas in [design-and-craft.md](design-and-craft.md) and [motion-and-faux-ui.md](motion-and-faux-ui.md), so it works even when none of them is installed. Install one only when the task needs its depth or tooling.

⚠️ **Before installing any of them:** skills can run scripts on your machine. Impeccable downloads and runs a binary and can add an edit hook; Oil UI runs an update check. Read what a skill runs before you install it, and install per project rather than globally if unsure.

| Skill | Use it for | Install | Licence |
|---|---|---|---|
| [Impeccable](https://github.com/pbakaus/impeccable) (Paul Bakaus) | Full design workflow with commands: shape, critique, audit, polish, harden, typeset, layout, clarify and more. Includes a "slop" detector you can run on a folder or URL. | `npx impeccable install` (detects your tools). Claude Code: `/plugin marketplace add pbakaus/impeccable`. Scan only: `npx impeccable detect src/` | Apache 2.0 |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (Next Level Builder) | Searchable database: styles, palettes, font pairings, 119 UX rules, chart types and stack-specific advice. Good for picking a starting design system. | Claude Code: `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill` then `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill`. Others: `npm install -g ui-ux-pro-max-cli` then `uipro init --ai codex` (or `claude`, `gemini`) | MIT |
| [Emil Kowalski's skills](https://github.com/emilkowalski/skills) | Motion and polish: animate, review-animations, remove-animations, choreograph, apple-design, mobile-native, break-ui (worst-case data), pick-ui-library, prototype. | `npx skills@latest add emilkowalski/skills` | MIT |
| [Oil UI](https://github.com/oil-oil/oil-ui) | Design method: a one-line "north star", one hero and one main action per screen, greyscale structure before colour, review from real screenshots. Written in Chinese, but replies in your language. | `npx skills add oil-oil/oil-ui` | MIT (the free edition; it mentions a paid Pro version) |
| [Stageshow](https://benji.org/stageshow) (Benji Taylor) | Faux product UI: believable product screenshots and animated demos for landing pages and feature cards, with filming and checking scripts. | `npx skills add benjitaylor/skills --skill stageshow` | MIT |
| [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) (VoltAgent) | Not a skill: a library of 84 DESIGN.md files analysing real sites (Linear, Stripe, Notion and others). | Copy one DESIGN.md into a project as a reference | MIT |

## Which to reach for

- **New page, no design system yet:** write a DESIGN.md first (see [design-and-craft.md](design-and-craft.md)). UI UX Pro Max or Impeccable's `shape` and `init` can help draft it.
- **Reviewing an existing UI:** run [ux-audit.md](ux-audit.md) first; add `npx impeccable detect` for a mechanical pass.
- **Animation work:** Emil Kowalski's `animate`, `review-animations` or `remove-animations`.
- **Marketing demo or hero illustration of the product:** Stageshow.
- **Stress-testing a component:** Emil Kowalski's `break-ui`.

## Using awesome-design-md safely

DESIGN.md is a plain markdown design system file (colours, type, spacing, components, do's and don'ts) that agents read before building UI. The format comes from Google Stitch. Use the collection to learn how a good DESIGN.md is structured, or to borrow an interaction pattern. Do not ship a site that copies another company's look, name or marks: it can mislead users and infringe their rights. Always write your own DESIGN.md from your own brand.
