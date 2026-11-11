
# Website and app build standards

Apply this to every website, app or coding task. Read only the sections the task needs; they follow this overview.

## House style

- British English, sentence case (headings included), degrees Celsius, metric units, no em dashes.
- Accuracy first. Never invent facts, figures, reviews, logos or legal claims. Flag anything uncertain with ⚠️, say why, and offer up to three possible answers marked as unconfirmed.
- Ask clear questions, and list them together at the end of the reply.

## Rules that always apply

1. **Evidence or it didn't pass.** Mark each checked item PASS, FAIL, N/A, UNSURE (say why) or MANUAL (say how to check). Cite file:line for code findings.
2. **The brand and the brief win.** A project's DESIGN.md or brand file overrides the "generated look" tells. Treat tells as prompts, not bans.
3. **Secrets stay on the server.** No secret key in frontend code, the app bundle or git history.
4. **Permissions live on the server or database**, never only in the UI.
5. **Ask before** making legal claims about a specific project, installing anything, deleting files, or changing more than was asked.
6. **Look at what renders.** Check the real page at desktop and phone widths before calling visual work done; if you can't, say "visual result not verified".

## Pick the task, then read

| Task | Read |
|---|---|
| Starting a new site or app | the "Legal and compliance (UK, EU, Spain, US)" section (start-here questions), the "Design and craft" section (parts 1 to 4), the "Security" section, then set up the project files below |
| Building or changing UI | The project's DESIGN.md, the "Design and craft" section, relevant items in the "UX audit (132 items)" section |
| "Audit the UX" or "review the app" | the "UX audit (132 items)" section, followed exactly: read-only, report table, then stop and ask which fixes to make |
| Security review or "harden this" | the "Security" section |
| Launching, or "is it ready?" | the "Launch checklist" section, the "Legal and compliance (UK, EU, Spain, US)" section, and the "App stores (Apple and Google)" section for native apps |
| "Could we get sued?" or a compliance audit of existing code | the "Compliance audit prompts" section (full audit first, read-only), then the "Legal and compliance (UK, EU, Spain, US)" section |
| Buying or setting up a domain or email sending | the "Launch checklist" section, domain setup |
| Animation, transitions or a product demo | the "Motion and faux UI" section |
| "What features could we add?" | the "Feature ideas (optional)" section |
| Needs more depth or tooling | the "Companion skills and design references" section |
| Checking where a rule came from | the "Sources" section |

## Set up every new project

Create or update these in the project root, and ask before overwriting anything:

1. **DESIGN.md**: the design system (structure in the "Design and craft" section, part 2).
2. **AGENTS.md** (read by Codex; Claude Code reads CLAUDE.md and Gemini CLI reads GEMINI.md by default, so put the same lines there too), containing at least:

```markdown
## Standards
- Follow the web-app-build-standards skill for all UI, security and launch work.
- British English, sentence case, no em dashes.
- Read DESIGN.md before any UI change.
- Secrets stay server-side; permissions are enforced on the server or database.
## Access control
(the access control matrix template from the security standards, filled in for this project)
```

## Reporting

Lead with what blocks launch or the main user journey. Sort findings HIGH (blocks sign up, onboarding, checkout, the core feature, or locks someone out), MEDIUM (friction elsewhere), LOW (polish). List MANUAL checks with how to do them. End with the questions, then stop before fixing unless told to go ahead; when fixing, do one change at a time and show the diff.

## UX audit (132 items)

Source: Stefano's saved UX audit prompt. Transcribed in full; only spelling was changed to British English (colour, centred, postcode) and headings to sentence case.

### Rules for running it

Work read-only: do not edit, install, delete, commit or deploy anything until the user approves the fixes at the end. Reading files and read-only commands (ls, grep, git log) are fine.

#### Step 1. Map the app

Say in a few lines: the framework, where routes or screens are defined, the component library or design system, and where shared styles or theme tokens live. Then list the main screens (home or landing, sign up and onboarding, the core feature screens, pricing, checkout, settings) with the file each one lives in. If there are more than 15, pick the 15 people use most and say which were skipped.

#### Step 2. Check every screen against every item

Read the actual components and styles, not just file names, and follow imports into shared components (Button, Input, Nav, Layout) to judge what actually renders. Note the file and line each answer is based on. If an item doesn't apply to a screen (no form, no pricing), mark it N/A and move on.

#### Step 3. Report back in this order

a) One table: Priority | Screen | Item # | What's wrong | Evidence | Suggested fix. Evidence is file:line. The fix is one line. List only items that fail or are UNSURE, sorted HIGH first, and name the screens that passed everything in one line under the table.

b) Priority: HIGH if it slows down or blocks the main action on a key screen (sign up, onboarding, checkout, the core feature) or locks someone out (accessibility); MEDIUM if it adds friction somewhere else; LOW if it's polish.

c) Things that can't be judged from code (real tap sizes on a phone, real load times, contrast on images, how a screen feels): list them as MANUAL, with how to check each one.

Never say an item passes without evidence; if it can't be told from the code, say UNSURE and why. No generic advice: every row points to a real file in the repo.

Then stop and ask which fixes to make. Change no file until the user says yes. When they do, fix them one at a time and show each diff.

### Part 1: UX laws

#### Hick's law
The more choices you give someone, the longer they take to decide, and that's when people leave.
1. One obvious main action per screen. Every screen should have one thing it wants people to do.
2. Make the main button look most important. It should outrank everything around it.
3. Hide advanced options until they're needed. Put them behind a "More" or "Advanced" toggle.
4. Never two buttons that look equally important. Two equal buttons make people stop and choose.
5. Don't show options that aren't relevant yet. Show them at the step where they matter.
6. Pick a default. The most common option should already be selected.
7. Highlight one pricing plan. If you have three plans, mark the one most people should pick.
8. Break long forms up. One question on each screen.
9. Five things or fewer in the main menu. Everything else can live one level down.
10. Group similar settings together. So people only see a few at a time.

#### Fitts's law
The smaller a button is and the further away it is, the longer it takes to tap, and every miss is another chance for someone to give up.
11. Make the main button big. Big enough to tap without looking.
12. Put it at the bottom of the screen. Where the thumb is already sitting.
13. Make the whole list row tappable. Not just the text or a small icon.
14. Keep delete far away from save. A missed tap shouldn't destroy anything.
15. Most-tapped means biggest and easiest to reach. Size and position should follow how often it's used.

#### Jakob's law
People spend most of their time in other apps, so they expect yours to work the same way. When it doesn't, it feels broken.
16. Logo top left, and it goes home. Tapping it should always take people to the start.
17. Cart and profile top right. That's where people look for them.
18. Use icons people already know. Like a magnifying glass for search.
19. Use the words people expect. A sign in button just says "Sign in".
20. Save your creativity for what only you do. Keep the basics standard.

#### The Von Restorff effect
The one thing that looks different is the thing people notice. When everything stands out, nothing does.
21. Make one thing on each screen look different. Different from everything else on it.
22. Make it different in one way. Like the colour or the size.
23. Keep everything around it plain. So it has something to stand out against.
24. Use it on the button that matters most. The one you most want people to press.
25. Highlight less. Every extra highlight makes the first one stand out less.

#### The goal-gradient effect
People speed up as they get close to the finish line, and if the finish line is hidden, they give up.
26. Show how many steps are left. From the very first step.
27. Start the progress bar a little full. So it feels like they've already started.
28. Make the last step the easiest one. Don't save the hard question for the end.
29. Put progress next to the button. Right beside the button they need to press.
30. Show the next goal straight away. The second they finish one, show how close the next one is.

#### The Doherty threshold
If your app responds in under 400 milliseconds, people stay focused. Any slower and their attention starts to drift.
31. Every tap does something right away. Even if it's just the button pressing down.
32. Show the change now, save it in the background. Don't make the screen wait for the server.
33. Start anything slow early. While they're still busy doing something else.
34. Show a grey outline while a page loads. A skeleton of the page, not a spinner.
35. Show a progress bar for anything slow. So people know it's still working.

### Part 2: More laws and principles

#### Miller's law
People can only hold a handful of things in their head at once. Miller put it at about seven; later research puts it lower.
36. Don't make people remember things between screens. Show the code, the price or the earlier choice again where it's needed.
37. Keep side-by-side comparisons short. A 20-row comparison table is a memory test.
38. Don't treat "seven" as a menu rule. It's about memory, not a magic number of menu items.

#### Chunking
Grouping small pieces into bigger, meaningful units makes them easier to read and remember.
39. Format long numbers in groups. Phone numbers, card numbers and codes: 4242 4242, not 42424242.
40. Break long text into short sections. With headings people can skim.
41. Split long lists into labelled groups. Ten settings in three groups beat ten in a row.

#### Cognitive load
Every bit of thinking your interface asks for uses up attention people would rather spend on what they came to do.
42. Cut anything that doesn't help the task. Decorations, extra links, repeated text.
43. Let people pick instead of remember. Show options to choose from rather than a blank box.
44. Do the maths for them. Show totals, dates and conversions already worked out.

#### The serial position effect
People remember the first and last items in a list best, and the middle ones least.
45. Put the most important items first and last. In nav bars, menus and feature lists.
46. Don't bury key actions in the middle. Of a long menu or a long page.
47. Open and close with what should stick. Your main benefit up top, your call to action at the end.

#### The Zeigarnik effect
People remember unfinished tasks better than finished ones, so a visibly incomplete task pulls them back.
48. Show what's left to do. A setup checklist with the unticked items showing.
49. Save progress automatically. So leaving never means starting over.
50. Bring people back to where they stopped. Resume, don't restart.

#### The peak-end rule
People judge an experience mostly by its most intense moment and by how it ended, not by the average.
51. Make your best moment great. Usually the first time the product actually works for them.
52. End every flow on a high note. A clear, friendly success screen after sign up or checkout.
53. Give the worst moments extra care. Errors, failed payments and cancelling.

#### Tesler's law
Every task has some complexity that can't be removed. The only question is whether the app handles it or the user does.
54. Let the app carry the complexity. Detect the country, format the phone number, fill the city from the postcode.
55. Don't simplify by removing what people need. Hiding a needed option just moves the work to them.
56. Pre-fill everything you already know. Name, email, last-used settings.

#### Postel's law
Be strict in what you send and flexible in what you accept. It started as a rule for internet protocols and works just as well for forms.
57. Accept input in any sensible format. Phone numbers with or without spaces, dashes or brackets.
58. Clean input up instead of rejecting it. Trim stray spaces, ignore capital letters in emails.
59. Be consistent in what you show back. One date format and one currency format everywhere.

#### The aesthetic-usability effect
People see good-looking designs as easier to use, and forgive small problems in them.
60. Polish the screens people see first. Landing, sign up and the first screen after it.
61. Keep spacing, colour and type consistent. Small inconsistencies read as "unfinished".
62. Watch what testers do, not what they say. A pretty screen can hide real problems.

#### The law of proximity
Things that are close together look like they belong together.
63. Put each label right next to its field. Closer to its own field than to the one above.
64. More space between groups than inside them. Spacing is how people see the groups.
65. Keep a button next to what it acts on. Not at the far end of the screen.

#### The law of similarity
Things that look alike seem to work alike.
66. Style everything clickable the same way. One look for links, one for buttons.
67. Don't style plain text like a link. Or a label like a button.
68. One colour, one meaning. If red means delete, don't also use it for "new".

#### The law of common region
Things inside the same border or background read as one group.
69. Use cards or panels to group related things. One card per item, one panel per topic.
70. Don't box things that aren't related. A shared box says "these go together".
71. Keep a section's actions inside its box. So it's clear what the button affects.

### Part 3: Checklists

#### Onboarding
72. Let people try it before signing up, where you can. Show the product working before asking for an email.
73. Ask only for what you need to start. Everything else can wait.
74. Get people to a first useful result fast. Count the taps from sign up to "oh, nice".
75. Teach by doing, not with a slideshow. Hints on the real screen beat a five-slide tour.
76. Let people skip optional steps. And finish them later.

#### Forms and input
77. Use one column. Fields side by side are easy to miss.
78. Labels above fields, not just placeholders. Placeholder text disappears the moment people type.
79. Bring up the right keyboard. Email, number and phone fields get the matching keyboard on mobile.
80. Support autofill and password managers. Set the right autocomplete attributes.
81. Check a field when people leave it. Not on every keystroke, and not only on submit.

#### Buttons and CTAs
82. Say what happens on the button. "Create account", not "Submit".
83. Start with a verb. Save, Send, Start free trial.
84. Stop double taps. Show a loading state and disable the button while it works.
85. Make buttons look like buttons. And links look like links.
86. Confirm only what can't be undone. Offer undo instead of "Are you sure?" on everything.

#### Navigation
87. Show where people are. Highlight the current tab or page.
88. Keep navigation in the same place everywhere. It shouldn't move between screens.
89. Make back always work. Browser back and swipe back shouldn't lose people's work.
90. Make search easy to find. If there's more than a few screens of content.
91. Use clear labels, not clever ones. "Pricing", not "Plans & Possibilities".

#### Feedback, loading and speed
92. Confirm every action. A checkmark, a toast or a changed state.
93. Offer undo for things people might regret. Archive, delete, send.
94. Stop the layout jumping as it loads. Reserve space for images and late content.
95. Say what's happening during long waits. "Uploading 3 of 10" beats a spinner.
96. Test speed on a mid-range phone. On a slow connection, not just your laptop on wifi.

#### Empty states
97. Never show a blank screen. Explain what will appear here.
98. Give one clear action to fill it. "Create your first project".
99. Offer an example or template. So people aren't starting from nothing.
100. Make "no results" helpful. Suggest a spelling fix, a wider filter or something related.
101. Treat "all done" as good news. An empty inbox should feel like a win.

#### Errors
102. Say what went wrong in plain words. Never just an error code.
103. Say how to fix it. "Use at least 8 characters", not "Invalid password".
104. Show the error next to the field. Not only in a banner at the top.
105. Keep what people typed. One error should never wipe a form.
106. Prevent errors before they happen. Date pickers, input limits, clear formats.

#### Mobile and thumb reach
107. Put main actions in easy thumb reach. The lower part of the screen.
108. Space tap targets apart. So people don't hit the one next to it.
109. Don't rely on hover. There's no hover on a touchscreen.
110. Don't hide key actions behind gestures only. Swipe-to-delete needs a visible option too.
111. Test it one-handed on a real phone. Not just in a desktop browser.

#### Accessibility
112. Text contrast of at least 4.5:1. 3:1 for large text (WCAG AA).
113. Tap targets of at least 44x44 points. Apple's guideline. Android's is 48x48 dp.
114. A visible focus state. Never remove the focus outline without a replacement.
115. Alt text on meaningful images. And empty alt text on decorative ones.
116. Respect reduced motion. Turn off big animations when the system setting asks.
117. Never use colour alone to carry meaning. Add an icon or text to red and green.

#### Typography and readability
118. Body text at least 16px on mobile. Smaller text gets skipped or zoomed.
119. Keep lines to roughly 50-75 characters. Long lines are hard to follow.
120. Line height around 1.5 for body text. Tight paragraphs are tiring.
121. One clear heading hierarchy. Each level clearly smaller than the last.
122. Left-align body text. Centred paragraphs are hard to read.

#### Copy and microcopy
123. Write the way you talk. Plain words, short sentences.
124. Say what it does for them. The outcome, then the feature.
125. One word for one thing. Don't call it a "project" here and a "workspace" there.
126. Cut every word that doesn't help. Then read it out loud.
127. Be specific. "Takes 2 minutes", not "quick and easy".

#### Trust and pricing pages
128. Show the real price up front. Including fees, before the last step.
129. Say what happens after the trial. When they'll be charged, and how much.
130. Make cancelling as easy as signing up. No hunting through settings.
131. Use real proof only. Real reviews, logos and numbers. Never made-up ones.
132. Make contact and refund info easy to find. A visible email or help link, not a maze.

## Design and craft

Labels: [Saved] from Stefano's saved reels; [Researched] checked against sources on 3 November 2026; [Practice] good practice; [Distilled] summarised from a companion skill (see the "Companion skills and design references" section).

### The rule that overrides the rest

**The brand and the brief win.** Every "tell" below is a default to question, not a ban. If a project's brand file chose a serif, a cream background, a full stop after a name or italics, keep it. What matters is that each visible choice was made for this project, not reached for by habit. [Distilled from Impeccable]

### 1. Decide before building

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

### 2. Keep a DESIGN.md in every project

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

### 3. Structure before style [Distilled from Oil UI]

- [ ] Give each screen one hero and one main action. Merge or demote anything competing with it.
- [ ] Sketch the main viewport in greyscale first: content order, main action and states. If the structure doesn't work in grey, colour and fonts won't save it.
- [ ] Build one representative page or the core flow with its key states, check it, then roll out.
- [ ] Use realistic content. Never fake customer reviews, results or metrics, and never leave "example" or "placeholder" text on screen.

### 4. Four patterns every app needs [Saved]

From the @haydenschmitty reel ("4 design patterns your vibe-coded app should be using").

1. **Skeleton loaders.** Grey bars in the shape of the layout while data loads. They cut perceived waiting time. Match the real content's geometry so nothing jumps.
2. **Semantic colours.** Besides the brand palette, define success, warning, danger and info, each with light to dark shades, and use them consistently. Not using them makes an app harder to read.
3. **Remove clutter.** AI tools love a two-sentence description under every heading ("My Day" does not need explaining). If it isn't tangibly useful, remove it.
4. **Accessibility.** The most common gap in vibe-coded apps, and one that can lead to complaints or legal action. Check against WCAG 2.2 AA (see the "Legal and compliance (UK, EU, Spain, US)" section).

### 5. Tells that make a design look generated

#### First wave [Researched]
- Purple or indigo fading to blue, including gradient headline text
- Inter, Geist or Roboto left as the default on everything
- Centred hero followed by three identical icon cards
- Identical rounded cards with the same soft grey shadow
- Emoji used as icons
- Glassmorphism, neon glow and 3D blobs
- Coloured left borders on cards
- Stock component library styling left untouched

#### Second wave [Researched]
Asking for "less AI" often produces these instead:
- Warm cream background, high-contrast serif and terracotta accent
- Near-black background with one acid-green or vermilion accent
- Broadsheet layout with hairline rules and square corners

#### Typography and structure [Researched]
- One accented word in a headline
- All-caps labels and an eyebrow above every heading
- Numbered markers such as 01, 02 and 03 when the content is not a sequence
- Meta strings joined with middle dots
- Monospace used for small labels as decoration
- An arrow added to every link or button
- Fade-and-slide animation on every section and hover effect on every card

#### 20 AI design slop indicators [Saved]
From the @charles.unemployed reel.

| | | | |
|---|---|---|---|
| 1. Tags and pills | 6. Overusing dividers | 11. Code breadcrumbs | 16. Squircles |
| 2. Excessive italics | 7. Colour shades and opacities | 12. Section numbering | 17. Excessive mono fonts |
| 3. Instrument Serif | 8. Containers with borders | 13. Eyebrows | 18. ALL CAPS subtitles |
| 4. Negative kerning | 9. Overly detailed diagrams | 14. Dithering | 19. Gradient backgrounds |
| 5. Over-the-top detailed UI | 10. Verbose, redundant text | 15. ASCII images | 20. Periods in titles |

#### Also refuse by default [Distilled from Impeccable]
- Same-size cards of icon, heading and text as the whole page structure; cards inside cards
- The hero-metric template: big number, small label, supporting stats
- A modal for a task that needs neither interruption nor protected focus
- Hard offset shadows (`4px 4px 0`) outside a genuinely neobrutalist brand
- Sparklines, progress rings and soft rounded boxes standing in for real content
- Unicode glyphs or emoji instead of one consistent icon set
- Light or dark chosen by category rather than by where and when people use it

#### Better habits [Researched]
- [ ] Give the hero something specific to the subject, not a large stat with a gradient accent.
- [ ] Keep line lengths under 80 characters.
- [ ] Make the visual hierarchy show what matters most.
- [ ] Limit automatic motion to one deliberate moment, and respect reduced motion settings.
- [ ] Keep visible keyboard focus and make layouts work on mobile.

### 6. Worked example: the OTP screen [Saved]

From the @charles.unemployed "Removing AI slop" reel, starting from the verification screen AI tools produce:

1. Remove the purple gradients and auto-submit when the last digit is entered. "Now it feels trustworthy."
2. Cut the extra words and drop the borders.
3. Improve the contrast of the digit tiles. (The reel also adds an iridescent background: a style choice, not a rule.)
4. Animate typing and give each state visual feedback: checking, wrong code (shown on the tiles, with text, not colour alone), verified.
5. Autofill the code from the text message (`autocomplete="one-time-code"` on the web), so nobody has to type.

### 7. Craft floor: check on the rendered page [Distilled from Impeccable]

- [ ] **Contrast:** body and placeholder text at least 4.5:1, large text 3:1. On coloured surfaces, tint secondary text from that colour, not grey.
- [ ] **Depth:** shadows have an offset and a soft blur; a zero-offset coloured glow is decoration.
- [ ] **Spacing:** tight inside groups, generous between them, more space above a heading than below it.
- [ ] **Type:** body lines about 65 to 75 characters; clear steps in size and weight; balanced headings; real copy tested at every breakpoint.
- [ ] **Motion:** one deliberate moment, not the same entrance on every section (see the "Motion and faux UI" section).
- [ ] **States:** hover, focus, disabled, loading, error and empty all designed.
- [ ] **Browser surfaces:** text selection colour, caret, scrollbars, focus rings, link underline offset and tabular numbers in data are themed, not left as defaults.
- [ ] **Copy:** controls name their action; errors name the problem and the fix.
- [ ] **Coverage:** every requirement in the brief is present and findable within seconds.

### 8. Copy [Researched]
- [ ] Cut empty words such as unlock, elevate and seamless.
- [ ] Never invent statistics, customers, logos or testimonials. This is also a legal risk.
- [ ] Say exactly what a button does: "Save changes", not "Submit".
- [ ] Keep the same word for an action throughout: "Publish" leads to "Published".
- [ ] Make errors explain what happened and how to fix it. They should not apologise or be vague.
- [ ] Make empty screens say what to do next.

### 9. Review what actually renders [Distilled from Oil UI and Impeccable]

- [ ] Look at screenshots at the sizes it ships at: desktop, about 390px and 360px phone widths, and 200% browser zoom.
- [ ] Judge "does it look right" and "does the task work" separately. Walk the main flow from its real entry point, save, reload and check it read back; force a failure and check the input was kept.
- [ ] Batch fixes, then look again, rather than screenshotting after every tweak.
- [ ] If a fresh reviewer (a subagent or a second model) is available, have it review the screenshots without seeing the code or the process.
- [ ] If screenshots aren't possible, say "visual result not verified" rather than claiming it looks right.

## Motion and faux UI

[Distilled] from Emil Kowalski's skills (motion) and Benji Taylor's Stageshow (faux product UI). For depth, install them (see the "Companion skills and design references" section).

### Should it animate at all?

| How often people see it | Decision |
|---|---|
| 100+ times a day (keyboard shortcuts, command menu) | No animation |
| Tens of times a day (hover, list navigation) | Remove or reduce a lot |
| Occasionally (modals, drawers, toasts) | Standard animation |
| Rarely (onboarding, celebrations) | Room for delight |

Every animation needs a reason: spatial consistency, showing a change of state, explaining something, feedback on a press, or avoiding a jarring jump. "It looks cool" is not a reason for something seen often. Never animate keyboard-triggered actions.

### Timing and easing

| Element | Duration |
|---|---|
| Button press feedback | 100 to 160 ms |
| Tooltips, small popovers | 125 to 200 ms |
| Dropdowns, selects | 150 to 250 ms |
| Modals, drawers | 200 to 500 ms |

- Keep interface animation under about 300 ms. Exits can be faster than entrances.
- Entering or exiting: ease-out. Moving on screen: ease-in-out. Never ease-in for interface motion; it feels slow.
- Use stronger custom curves than the CSS defaults, for example `cubic-bezier(0.23, 1, 0.32, 1)` for ease-out.
- Stagger groups by 30 to 80 ms rather than showing everything at once.

### Review checklist

| Issue | Fix |
|---|---|
| `transition: all` | Name the exact properties |
| Entry from `scale(0)` | Start from `scale(0.95)` with `opacity: 0` |
| Popover grows from its centre | Set `transform-origin` to the trigger (modals stay centred) |
| Hover effects on touch devices | Wrap in `@media (hover: hover) and (pointer: fine)` |
| Keyframes on something triggered rapidly | Use transitions, which can be interrupted |
| Animating width, height or top | Animate `transform` and `opacity` |
| No reduced-motion handling | Respect `prefers-reduced-motion`: replace movement with a fade or nothing |

Test gestures (drawers, swipes) on a real phone.

### Faux product UI for marketing pages (Stageshow)

For hero images, feature cards and demo animations that show the product.

**The idea:** it reads as a real product, simplified to what the viewer needs, framed with intent, and every motion has a cause.

**Five ways it fails:**
1. **Too much:** real text in every row, numbers everywhere. More detail looks more generated.
2. **Wireframe:** two grey blobs and a button; stripped of what made it recognisable.
3. **Boxed:** a whole window shrunk into a card with even margins, like a pasted screenshot.
4. **Flat:** every object the same weight; the eye has nowhere to land.
5. **Bland:** a grey window with a cursor, ignoring the brief's look.

**How to do it:**
- Plan first: where it sits, the focal object, the action, the payoff, what to leave out.
- Use real words only where the story is (usually 3 to 7 strings); placeholder lines elsewhere.
- Crop windows and phones off the edge of the frame; don't float a whole device with air on four sides.
- Tell a story in three to five beats over 10 to 16 seconds; no cursor move you can't explain; the loop ends where it began.
- Make the still (poster) frame tell the story on its own: many people only see that frame.
- Use the product's own icons and chrome. No sparkles, purple or invented logos. Borrow other products' interactions, never their identity.
- Check it at phone width too, with a design made for that width, not a squeezed one.

## Security

Labels: [Saved] from Stefano's saved reels and links; [Researched] checked against sources on 3 November 2026; [Practice] good practice; ⚠️ verify before relying on it. This is a working checklist, not a security audit.

### Five one-minute checks [Saved]

From Lincoln Devine's guide ([lincolndevine.com/guides/secure](https://lincolndevine.com/guides/secure/)). AI coding agents often take shortcuts that make an app work but leave it open; the app runs and tests pass, so nothing looks wrong.

1. **Database access:** in Supabase, is row-level security off on any table? If so, anyone with the public key may read it.
2. **Firebase rules:** are they still in permissive test mode?
3. **Secret keys:** search the source for service-role and secret keys. Server keys must never reach the browser. If one leaked, rotate it and scan the git history.
4. **Server-side authorisation:** log out and call the data endpoints in a browser. If data still loads, the check lives only in the interface.
5. **Storage buckets:** are uploaded files public, especially with guessable file names?

Dashboard settings (RLS toggles, Firebase rules in the console, bucket visibility) can't be seen by an agent reading code. Ask the user to check them, or use the provider's CLI if it is connected. Report findings ranked by blast radius: what an attacker could reach, and how many users it affects.

### Two hands-on tests: shared URLs and logout [Saved]

From a @securedbycasco reel, where the engineer answers a viral "why you shouldn't trust vibe-coded apps" video.

1. **Insecure direct object reference (IDOR).** Signed in as user A, copy the URL of one of their records (for example `app.com/mail/a8f3e1c9`). Sign in as user B in another browser and open it. If B sees A's data, the app exposes an object ID in the URL or request but never checks that the user is authorised to see it. Change the ID, reach someone else's data. This is OWASP "broken access control" (CWE-639). Fix it on the server or database, not by hiding the link.
2. **Logout.** Sign in, copy a private URL, log out, then paste the URL again. If it still loads, or the backend still accepts the old token, logout is cosmetic. A proper logout clears all four (the session token, auth and session cookies, localStorage and sessionStorage) and then invalidates the token on the server, so it can't be reused from any device.

### Hardening prompt, corrected [Saved]

From a @securedbycasco reel, where a security engineer reacts to a popular prompt. The original asked to "review this app and harden its security" with: rate limiting on all public endpoints (IP and user-based, sensible defaults, graceful 429s); strict input validation and sanitisation on all user inputs (schema-based, type checks, length limits, reject unexpected fields); and secure API key handling (remove hard-coded keys, move to environment variables, rotate keys, no keys client-side), following OWASP, with clear comments and without breaking existing functionality.

The engineer's corrections:
- Public endpoints often serve people who aren't signed in yet, so user-based rate limits do little there. Limit by IP and other signals too.
- Keeping keys in environment variables isn't enough. Any call that uses an API key belongs on your server, or better, uses short-lived credentials.
- Put the rules in the project's standing rules file (CLAUDE.md, AGENTS.md, GEMINI.md, Cursor rules), not only in one prompt.
- Write an access control matrix into that file. Most security problems in vibe-coded apps come from the agent not knowing the expected behaviour, not from bad code.

#### Access control matrix template

Add to the project's CLAUDE.md or AGENTS.md and keep it current:

```markdown
## Access control
| Resource | Signed out | User | Owner of the record | Admin |
|---|---|---|---|---|
| Public pages | read | read | read | read |
| Profile | none | read own | read, edit, delete | read, suspend |
| Bookings | none | create | read, cancel own | read, cancel any |
Rules: enforce on the server or database, never only in the UI. Anything not listed is denied.
```

### Secrets, access and hardening [Researched and Practice]

#### Secrets
- [ ] Never put secret keys in frontend code or the app bundle. Examples are AI API keys, Stripe secret keys, Supabase service-role keys, database credentials and private signing keys.
- [ ] Know the difference: Stripe publishable keys and Supabase anon keys are designed to be public, but their safety depends on correct permissions.
- [ ] Add `.env*` to `.gitignore` before committing.
- [ ] If a secret was committed, rotate it and clean the history. Deleting the latest commit is not enough.
- [ ] Check public environment variables, such as anything prefixed `NEXT_PUBLIC_`.
- [ ] Scan before launch, for example with `semgrep --config=p/secrets --config=p/owasp-top-ten .`

#### Access control
- [ ] Enforce permissions on the server or database, never only in the browser.
- [ ] Turn on row-level security on every Supabase table holding user data, with policies limited to the correct user. In Firebase, set equivalent security rules.
- [ ] Test as a logged-out user and as a second user. Change an ID in a request and confirm you cannot see someone else's data.
- [ ] Check authentication on every API route.
- [ ] Logging out clears the session token, cookies, localStorage and sessionStorage, and invalidates the token server-side.

#### Hardening [Practice]
- [ ] Validate all input on the server.
- [ ] Keep detailed errors in server logs and out of API responses.
- [ ] Set security headers, including Content-Security-Policy, HSTS and clickjacking protection.
- [ ] Do not use overly permissive CORS.
- [ ] Add rate limits to login, forms and costly AI endpoints.
- [ ] Set spending limits on paid APIs.
- [ ] Run dependency audits, such as `npm audit`, and review what an AI tool installed.
- [ ] Review the app against the OWASP Top 10. ⚠️ Check the latest edition directly.

#### Working with AI coding tools [Practice]
- [ ] Read and test the code. Passing a demo does not make an app secure.
- [ ] Use version control, and commit before major AI changes.
- [ ] Keep test and production data separate. Never use real personal data for testing.
- [ ] Do not paste live secrets or personal data into AI chats.
- [ ] Test the main user journeys and failure states before launch.
- [ ] Set up backups and test a restore.

## Legal and compliance (UK, EU, Spain, US)

Labels: **[Saved]** from Stefano's saved reels and files; **[Researched]** checked against sources on 3 November 2026 (US section: 10 November 2026; marketing email and minimum age: 11 November 2026); **[Practice]** good practice, not a legal rule; **⚠️** weaker source, background knowledge or likely to change, so verify before relying on it.

This is a working checklist, not legal advice. Have a solicitor check anything high-risk, particularly payments, health data, children's data or user-generated content. Ask before making legal claims about a specific project.

### Start here: which rules apply?

Answer these before building:

- Who is the legal operator, and where is it established?
- Does the site or app target people in the UK, the EU, the US, or a mix?
- Does it collect personal data, including through forms, analytics or embeds?
- Does it sell anything to consumers? Is it a one-off purchase or a subscription?
- Could under-18s use it?
- Can users post content or talk to each other?
- Does it use an AI chatbot or publish AI-generated content?
- Does it handle health or other special category data?
- Does it send marketing email, sell a subscription, or let users upload content others can see?

For a quick scan of an existing codebase, run the full audit prompt in the "Compliance audit prompts" section.

### UK rules [Researched]

#### Company details
- [ ] A UK limited company shows on its website its registered name, registered number, part of the UK where it is registered, and registered office address. The rules sit in the Company, Limited Liability Partnership and Business (Names and Trading Disclosures) Regulations 2015.
- [ ] If VAT registered, show the VAT number. ⚠️ Based on a law firm note, so confirm with the accountant.
- [ ] Copy the details exactly from the Companies House register.

#### Cookies and tracking (PECR)
- [ ] Audit more than cookies. The ICO's April 2026 guidance also covers tracking pixels, link decoration, local storage, fingerprinting, scripts and tags.
- [ ] Get consent before setting anything non-essential, unless a specific exception applies.
- [ ] Newer exceptions, in force since 5 February 2026, can cover limited statistical analytics and remembering appearance preferences such as language or dark mode.
- [ ] To rely on the statistical exception, tell users clearly and give them a simple, free way to object. Any provider must act only on your behalf and not use the data for its own purposes.
- [ ] Assume default Google Analytics needs consent. ⚠️ Based on vendor commentary, so check the current ICO text and configuration.
- [ ] Advertising trackers need consent. The ICO has looked at relaxing enforcement for low-risk advertising, but do not assume that applies. ⚠️ This area may change.
- [ ] Session replay and heatmap tools (Hotjar, FullStory, LogRocket, Microsoft Clarity and similar) are non-essential: load them only after consent, mask every input by default, and switch replay off on sign-up, login, checkout and account pages. [Saved] [Practice]
- [ ] Fines under PECR now align with UK GDPR levels, up from the old £500,000 cap (about €575,000 ⚠️ approximate conversion).

#### Data protection (UK GDPR and Data Protection Act 2018)
- [ ] Give a clear privacy notice covering who you are, what you collect, why, your lawful basis, who receives it, retention, transfers and user rights. ⚠️ Background knowledge.
- [ ] Add a data processing agreement with each supplier that handles personal data for you. ⚠️ Background knowledge.
- [ ] Check whether the ICO data protection fee is due. ⚠️ Not verified in this research.

#### Accessibility (Equality Act 2010)
- [ ] Treat accessibility as a legal duty. Service providers must make reasonable adjustments and anticipate disabled people's needs.
- [ ] Do not describe WCAG as a law for private companies. The Act names no technical standard, but WCAG AA is the usual benchmark in practice.
- [ ] Build to WCAG 2.2 AA. This also covers the WCAG 2.1 AA level used in the EU.

#### Consumer law (DMCC Act 2024)
- [ ] Do not write, commission or publish fake reviews or concealed incentivised reviews. This applies to businesses of all sizes.
- [ ] Do not publish genuine reviews in a misleading way, such as hiding negative ones without saying so.
- [ ] Remove misleading claims, pressure tactics and hidden compulsory fees. The CMA can fine directly, up to 10% of global turnover.
- [ ] If selling at a distance, check pre-contract information and the 14-day cancellation rules. ⚠️ Confirm how they apply to the specific product.
- [ ] If selling subscriptions, check the new DMCC regime. ⚠️ One law firm says it is expected in January 2027, so verify the date and final rules.

#### Children and user-generated content
- [ ] If under-18s are likely to use the service, apply the ICO Children's Code and its 15 standards, and carry out a data protection impact assessment.
- [ ] A tick-box asking users to state their age may not be enough. The ICO has criticised this on services with user interaction and user-generated content.
- [ ] If users can post or interact, check the Online Safety Act 2023 and Ofcom's guidance.

#### Marketing email and texts (PECR regulation 22) [Researched]
- [ ] To individuals (including sole traders and partnerships), marketing email or texts need prior consent, unless the soft opt-in applies.
- [ ] Soft opt-in: you got the details directly from the person in the course of a sale or negotiations for a sale, you only market your own similar products or services, and you gave a simple way to refuse when you collected the details and in every message since.
- [ ] Put a prominent opt-out or an unticked opt-in box on the form itself. The ICO says an opt-out hidden in the privacy policy isn't enough.
- [ ] For waitlists and newsletter sign-ups, get explicit consent with an unticked box and keep a record of it. ⚠️ Whether a waitlist sign-up counts as "negotiations for a sale" for the soft opt-in is untested; don't rely on it. [Practice]
- [ ] Every message must say who it is from and give a valid address or link to opt out, free of charge. Act on opt-outs promptly.
- [ ] Emails to company addresses (limited companies, LLPs) don't need PECR consent, but you must still identify yourself and offer an opt-out, and UK GDPR still applies to named people's addresses.
- [ ] Since 5 February 2026 there is also a charitable purposes soft opt-in, for registered charities only.
- [ ] PECR fines are now up to £17.5 million (about €20 million ⚠️ approximate conversion) or 4% of global turnover.

### EU rules [Researched]

#### Cookies and data protection
- [ ] Apply the GDPR and the national ePrivacy rules. A UK company targeting EU users may still be caught. ⚠️ Confirm for the specific project.
- [ ] Do not build to the proposed Digital Omnibus cookie or GDPR changes. As of October 2026 the proposal was still at first reading. ⚠️ Recheck before launch.
- [ ] Consider whether an EU representative is needed under GDPR Article 27 if there is no EU establishment. ⚠️ Background knowledge.

#### Marketing email (ePrivacy Directive Article 13)
- [ ] Same shape as the UK: prior consent for marketing email to individuals, with a soft opt-in for existing customers about similar products, and an opt-out at collection and in every message. ⚠️ Background knowledge; rules for business addresses vary by country, so check each market.
- [ ] Spain is stricter: see the Spain section below.

#### Minimum age and parental consent (GDPR Article 8) [Researched]
- [ ] If you rely on consent to process a child's data for an online service offered directly to children, a child below the national "digital age of consent" needs a parent's consent, and you must make reasonable efforts to verify it.
- [ ] The default is 16. Countries can lower it to 13. Thresholds found in November 2026: UK 13; Spain, Italy, Austria 14; France, Greece, Czech Republic 15; Germany, Ireland, Netherlands 16; Belgium, Denmark, Sweden, Finland, Portugal 13. ⚠️ Sources disagree on a few countries, and Spain has a draft law to raise its age to 16, so recheck before launch.
- [ ] Default for the sign-up age screen in Stefano's projects:
  - UK only: 13.
  - Spain only: 14.
  - Several EU countries, or UK and EU together, with no per-country logic: 16. It is the highest threshold, so it is valid everywhere.
  - Below the threshold, either block sign-up or collect verified parental consent. Don't just tick a box.
- [ ] Article 8 is a consent rule, not a ban: if the lawful basis is something else (such as contract), the threshold works differently. ⚠️ Get advice before relying on that.
- [ ] Separately, the UK Children's Code and the Online Safety Act protect everyone under 18. Passing the age screen doesn't switch them off. If the app is built for under-18s, skip the age gate and design for the Children's Code, with legal review.

#### Third-party fonts [Saved]
- [ ] Self-host every font. Loading from fonts.googleapis.com or fonts.gstatic.com sends each visitor's IP address to Google before they have agreed to anything. Vibe-coded apps do this by default.
- [ ] The case: in January 2022 the Munich Regional Court (LG München I) found this breached the GDPR and awarded the visitor €100 in damages. It set off a wave of demand letters in Germany.
- [ ] ⚠️ One saved reel quotes "fines up to €250,000 per violation". That figure was the penalty the court threatened if the site kept doing it after the ruling, not a fine per visitor. Don't repeat it as a GDPR fine.
- [ ] The same reasoning applies under UK GDPR, since an IP address is personal data. ⚠️ No UK ruling on this found; treat it as a risk, not settled law.
- [ ] Check other third-party CDNs too (icon fonts, Adobe Fonts, script CDNs), and packages or themes that pull fonts in without an obvious link tag.
- [ ] Verify in the browser: Network tab, reload, filter for "google". Nothing from either font domain should appear. Prompt in the "Compliance audit prompts" section.

#### Accessibility (European Accessibility Act)
- [ ] Check whether the service is covered. The Act has applied since 28 June 2025 and covers e-commerce services sold to EU consumers, including from outside the EU.
- [ ] Use WCAG 2.1 AA, through EN 301 549, as the working standard. ⚠️ EAA-specific harmonised standards were reported as still being finalised, and native apps have extra requirements.
- [ ] Check the microenterprise exemption for services. ⚠️ From background knowledge, it covers fewer than 10 staff and no more than €2m in annual turnover or balance sheet total. It does not cover products. Build accessibly anyway, because UK duties still apply.
- [ ] If in scope, publish the required accessibility information. ⚠️ Confirm the format under national law.

#### Consumer sales
- [ ] If consumers can buy online and have a withdrawal right, provide an online withdrawal function. This has applied since 19 June 2026 with no small business exemption.
- [ ] Make it clearly labelled and easy to find, send an automatic confirmation, and record the date and time.
- [ ] Update the privacy notice for data collected through that function.
- [ ] Do not offer email or phone as the only route. Check national implementation. ⚠️ Timing and details vary by country.

#### AI (EU AI Act, Article 50)
- [ ] Article 50 transparency duties have applied since 2 August 2026. Tell users when they are talking to an AI system, unless it is obvious. ⚠️ Check the exact scope and exceptions.
- [ ] Check whether AI-generated content needs labelling or machine-readable marking. Providers of systems already on the market before 2 August 2026 have until 2 December 2026 for marking. ⚠️ Check whether you count as a provider or deployer.

#### Online platforms
- [ ] If the service hosts user content or is a marketplace, check the Digital Services Act. ⚠️ Not fully verified here, including reliefs for small businesses.

### Spain (if targeting Spanish users)

- [ ] Follow Article 22.2 of the LSSI (Ley 34/2002) on cookies and the AEPD's cookie guide. Provide clear information and get valid consent before non-exempt cookies are used.
- [ ] Block non-exempt cookies until consent. ⚠️ Based on a practitioner source, so check the current AEPD guide.
- [ ] Check the aviso legal details required by Article 10 of the LSSI. ⚠️ Not fully verified here.
- [ ] Marketing email (LSSI Article 21) [Researched]: prohibited unless the person asked for it or expressly agreed beforehand. Tacit consent isn't accepted. The AEPD applies this to companies' addresses as well as individuals'.
- [ ] The only exception: an existing contract with the person, marketing your own products or services similar to what they bought.
- [ ] Offer a simple, free opt-out when collecting the address and in every email. The email must include an email address or other valid electronic address for opting out.
- [ ] The AEPD fines this regularly, from a few thousand euros for continuing after an unsubscribe to €20,000 for sending without consent.
- [ ] Minimum age for consent: 14 (Organic Law 3/2018, Article 7). See the EU minimum age section above.
- [ ] Check Spanish consumer law for any sales, including the withdrawal function. ⚠️ Not fully verified here.
- [ ] Add other countries only after checking their local rules.

### US (if targeting US users) [Saved]

From the "How to protect your vibe coded app from getting sued" guide (the six legal holes). Figures and dates checked on 10 November 2026; see the "Sources" section. US rules can reach a UK or EU operator whose app is used by people in the US. Copy-paste fix prompts are in the "Compliance audit prompts" section.

#### Session replay and wiretapping (California, CIPA)
- [ ] Plaintiffs sue under the California Invasion of Privacy Act, arguing a third-party tool recording what visitors type is like tapping a phone call. Statutory damages are $5,000 (about €4,300 ⚠️ approximate conversion) per violation.
- [ ] SB 690, signed on 30 September 2026, ends private lawsuits over pen-register and trap-and-trace claims (the tracking pixel theory) for websites and apps. It does not touch the wiretapping (§631) and eavesdropping (§632) sections that session replay claims rely on. [Researched] ⚠️ One source says it takes effect on 1 January 2027.
- [ ] Fix: mask every input in replay tools, exclude passwords, payment fields and personal data, and load trackers only after consent. Check the tool's dashboard too: a project-level setting can override the code.

#### Children under 13 (COPPA)
- [ ] COPPA applies if the app is aimed at children, or you actually know a user is under 13. Then you need verified parental consent before collecting their data.
- [ ] Civil penalties reach $53,088 (about €46,000 ⚠️ approximate conversion) per violation. [Researched] ⚠️ The FTC made no inflation adjustment for 2026, according to a secondary source; check 16 CFR 1.98.
- [ ] The amended COPPA Rule had a compliance date of 22 April 2026.
- [ ] For a general-audience app, use a neutral age screen: an empty date of birth field that doesn't hint at the required age (not an "I am over 13" tick-box). If under 13, don't create the account, store nothing they entered, and set a flag so they can't immediately retry with a different date. If 13 or over, store an "age verified" flag rather than the full date unless the app needs it.
- [ ] Check landing pages, app store listings and marketing for anything aimed at children.
- [ ] If the app is meant for children, stop and get a lawyer. Note the UK Children's Code covers under-18s, a much wider group than COPPA.

#### Marketing email (CAN-SPAM, plus Gmail and Yahoo rules)
- [ ] Covers launch emails, newsletters and promotions, even to people who joined your waitlist. Each non-compliant email can be a separate violation, up to $53,088.
- [ ] Every marketing email needs a real postal address (a registered PO box or mailbox service counts), a clear unsubscribe link that works without logging in, a truthful subject line and a real from name.
- [ ] Honour unsubscribes within 10 business days, across every marketing list, and make the send code skip them.
- [ ] Since 2024, bulk senders (more than 5,000 a day to Gmail) need one-click unsubscribe headers: `List-Unsubscribe` and `List-Unsubscribe-Post: List-Unsubscribe=One-Click`. Most providers (Resend, Loops, ConvertKit, Mailchimp) handle this once turned on.
- [ ] Send the launch email to yourself first and test the unsubscribe link.
- [ ] Transactional email (receipts, password resets) is treated differently; list it, but don't add marketing footers to it.

#### Subscriptions and auto-renewal (ROSCA, California ARL)
- [ ] Federal ROSCA: show all material terms before taking card details, get clear consent, and give a simple way to cancel. The FTC is actively enforcing it.
- [ ] California's amended Automatic Renewal Law, in force since 1 July 2025: express affirmative consent to the auto-renewal terms; keep proof for three years or one year after the contract ends, whichever is longer; send an annual reminder; give 7 to 30 days' notice of a price increase. [Researched]
- [ ] Next to the pay button, show the price, how often it is charged, that it renews until cancelled, when the first charge happens (including when a trial ends), and how to cancel.
- [ ] Offer online cancellation as easy as signing up (for Stripe, the customer portal with cancellation on), send a confirmation email repeating the terms, and store a consent record (timestamp, terms shown, plan).
- [ ] The five-second test: could a stranger tell what they pay, how often, and how to stop?
- [ ] ⚠️ The FTC's 2024 "click to cancel" rule was struck down by a federal appeals court in July 2025 (background knowledge, not rechecked); ROSCA and state laws still apply.

#### User uploads (DMCA safe harbour, CSAM reporting)
- [ ] If users can upload content others can see, the DMCA safe harbour only protects you if it is set up properly. A disclaimer alone isn't enough.
- [ ] Register a designated agent with the US Copyright Office: $6 (about €5 ⚠️ approximate conversion), valid for three years, so diary the renewal. [Researched] The agent can be you, a role such as "Legal Team", or a service. ⚠️ The guide says a PO box works for the address; one law firm says the service provider's own address must be a physical street address, so check the form.
- [ ] Publish a /copyright page with the agent's details and what a valid notice must include, add a Report button on every piece of user content, and write a repeat infringer policy into the terms (for example, suspension after three valid strikes).
- [ ] Put a line under upload forms: only upload content you own or have permission to share.
- [ ] US law requires platforms to report child sexual abuse material to NCMEC when they become aware of it. For image-heavy apps, look at a scanning service (Cloudflare's CSAM Scanning Tool is free for Cloudflare users) and get legal advice on the reporting process. In the UK, also check the Online Safety Act duties above.

#### Privacy policy (CalOPPA)
- [ ] California's online privacy law requires a privacy policy if you collect personal information from California residents, which in practice means any app with a sign-up form.
- [ ] Draft it from what the code actually collects and shares, not a template, and mark points for lawyer review.

## Compliance audit prompts

Copy-paste prompts for an AI coding tool that can read the whole project (Claude Code, Codex, Cursor, Gemini CLI). Adapted from the "How to protect your vibe coded app from getting sued" guide [Saved], widened to cover UK and EU rules. The rules behind each prompt, with sources and caveats, are in the "Legal and compliance (UK, EU, Spain, US)" section. This is a working checklist, not legal advice.

You'll need: the code open in the tool, access to the email provider, Stripe and analytics dashboards, and about two hours. Most fixes take 5 to 15 minutes. If users can upload files, budget $6 (about €5 ⚠️ approximate conversion) for the DMCA agent registration.

### 1. Full audit (run first, changes nothing)

```text
Audit this codebase for common legal compliance risks. Do not change any code. Read the whole project and, for each item below, report FOUND, NOT FOUND or UNSURE, the exact files and line numbers, and a one-sentence fix.

1. Fonts: anything loaded from fonts.googleapis.com, fonts.gstatic.com or another third-party font or asset CDN, including CSS @import, <link> tags, packages and themes.
2. Third-party tracking: every analytics, session replay, heatmap or chat widget script (for example Hotjar, FullStory, LogRocket, Microsoft Clarity, PostHog, Mixpanel, Google Analytics, Intercom). For each, say whether it can record keystrokes or form inputs, and whether it loads before consent.
3. Consent: is there a consent banner, are Accept and Reject equally easy, and do non-essential scripts, cookies, pixels and local storage actually wait for consent?
4. Age: does sign-up ask for age or date of birth? Is any part of the app or its marketing aimed at children?
5. Email: every place the app sends marketing or newsletter email. Does each template include a postal address, a working unsubscribe link and List-Unsubscribe headers? Does the send code skip unsubscribed people?
6. Subscriptions: every checkout or pricing page with a recurring charge or a trial that converts to paid. Are the price, frequency, renewal terms, first charge date and how to cancel shown next to the pay button? Can users cancel online? Is consent recorded?
7. User uploads: every place users can post files, images or text others can see. Is there a terms of service, a copyright takedown page and a Report button?
8. Legal pages and business details: is there a privacy policy, terms, cookies policy and, where relevant, refund policy and company details, linked from the footer and the sign-up form?
9. Access control: can one user open another user's record by changing an ID in a URL or request, and does logout invalidate the session on the server?

Finish with a table ranked from highest to lowest risk. Mark anything you can't judge from code as MANUAL, with how to check it.
```

Save the report and work through the fixes below one at a time.

### 2. Self-host fonts

```text
Find every font this project loads from Google Fonts or any other external font service. For each one:
1. Download the exact woff2 files for the weights and styles actually used.
2. Save them under /fonts in the public or static folder.
3. Replace the external <link> or @import with local @font-face rules using font-display: swap.
4. Remove every remaining reference to fonts.googleapis.com and fonts.gstatic.com.
If this is a Next.js project, use next/font/local instead.
Then search the whole project, including node_modules, CSS and config files, and confirm no external font domains remain. If a package or theme still loads them, tell me which one.
```

Check: open the live site, Network tab, reload, filter for "google". Nothing from either font domain should load.

### 3. Mask session replay and gate tracking on consent

```text
For every analytics, session replay or heatmap tool in this project:
1. Turn on input masking so no keystrokes or form values are ever recorded. Use the tool's own setting (for example maskAllInputs, data-hj-suppress, fs-mask) and mask every input, textarea and contenteditable element by default.
2. Exclude passwords, payment fields, email addresses and other personal data from recordings entirely.
3. Load the tool only after the user accepts in a consent banner. If there is no banner, add one with Accept and Reject buttons that are equally easy to use, and remember the choice.
4. Switch session replay off completely on sign-up, login, checkout and account settings pages.
Show me every change.
```

Check: in the tool's dashboard, confirm the project-level privacy setting matches, then record a test session and type a fake email to confirm it is masked.

### 4. Neutral age screen

```text
Add a neutral age screen to the sign-up flow:
1. Ask for date of birth with an empty date picker. Do not pre-fill it or say what age is required.
2. Use this minimum age: [13 for UK-only or US-only; 14 for Spain-only; 16 if the app serves several EU countries, or the UK and EU together, without per-country rules]. If the user is under it, do not create the account and do not store the date of birth, email or anything else they entered. Show a polite message that the app isn't available for their age.
3. Set a cookie or local storage flag so they can't immediately go back and enter a different date.
4. If they are old enough, continue sign-up and store only an "age verified" flag unless the app needs the full date.
Also list anything in the landing page, app store listing or marketing copy that could look aimed at children.
```

The defaults come from GDPR Article 8 and COPPA; see the minimum age section in the "Legal and compliance (UK, EU, Spain, US)" section. Below the minimum, the alternative to blocking is verified parental consent. If the app is meant for under-18s (including 14 to 18-year-olds), don't use this gate: design for the UK Children's Code and get legal review. A self-declared age may not be enough there.

### 5. Marketing email

```text
Audit every marketing, newsletter and announcement email this app sends. List transactional emails (password resets, receipts) separately but don't change them.
For each marketing template:
1. Add a footer with the business name and postal address: [ADDRESS].
2. Add a clear unsubscribe link that works without logging in.
3. Add List-Unsubscribe and List-Unsubscribe-Post: List-Unsubscribe=One-Click headers if the provider supports them.
4. Make sure the subject line isn't misleading and the from name is the real business name.
Then check that unsubscribing removes the person from every marketing list and that the send code skips them. Show me where that check happens.
Finally, check how addresses get onto marketing lists. Every sign-up, waitlist or checkout form that adds someone to marketing must have an unticked opt-in box (or, for existing customers only, a clear opt-out at the point of collection), and the database must store when and how each person agreed. List any form that adds people to marketing without this.
```

UK and EU rules need consent before the first marketing email, not just an unsubscribe link afterwards; Spain accepts no tacit consent at all. See the marketing email sections in the "Legal and compliance (UK, EU, Spain, US)" section.

Check: send the launch email to yourself first and click unsubscribe.

### 6. Subscription checkout

```text
Audit every checkout and pricing page that sells a recurring subscription or a free trial that converts to paid.
1. Next to the purchase button, show in plain text: the price, how often it is charged, that it renews automatically until cancelled, when the first charge happens (including when a trial ends), and exactly how to cancel.
2. If we use Stripe Checkout, add this with custom_text near the submit button, and set consent_collection for terms of service so the user must tick a box before paying.
3. Add online cancellation as easy as signing up. With Stripe, turn on the customer portal with cancellation enabled and link to it from the account page.
4. Send a confirmation email after purchase repeating the terms and how to cancel.
5. Store a consent record for each user (timestamp, terms shown, plan) in the database.
Show me the checkout page before and after.
```

Check: could a stranger tell in five seconds what they pay, how often, and how to stop? If Stripe won't show the custom text in your Checkout mode, put the terms on your own pricing page directly above the button that sends people to Stripe.

### 7. User uploads

```text
Set up user content protection:
1. Create a /copyright page explaining how to send a copyright takedown notice, with our designated agent's name, address and email: [AGENT DETAILS FROM THE COPYRIGHT OFFICE REGISTRATION]. List what a valid DMCA notice must include.
2. Add a Report button on every piece of user-uploaded content that sends the report to an admin queue.
3. Add an admin action to remove reported content and track strikes per user. After 3 valid copyright strikes, suspend the account. Write this repeat infringer policy into the terms of service.
4. Under every upload form, add: "Only upload content you own or have permission to share. See our Terms and Copyright Policy."
5. Link the Terms of Service and Copyright Policy in the footer.
```

Register the agent at copyright.gov first ($6, renew every three years). For image uploads, also plan for CSAM detection and reporting, and in the UK check the Online Safety Act.

### 8. Privacy policy and terms from the real code

```text
Read this whole codebase and list every piece of personal data the app collects (including what third-party tools such as analytics, Stripe and the email provider collect), where it is stored, and who it is shared with. Then draft a plain-English privacy policy and terms of service based on what the app actually does, not a generic template. Cover UK GDPR and, where relevant, EU GDPR and California rules. Mark every point a lawyer should review with [LAWYER REVIEW]. Add both pages and link them in the footer and next to the sign-up button.
```

An AI draft based on the real code beats a copied template, but it is still a draft: have a lawyer check it before you scale.

### 9. Access control and logout

```text
Check access control and logout. Do not change code yet.
1. List every route or endpoint that takes a record ID (in the URL, query or body). For each, show where the server checks that the signed-in user is allowed to see or change that record. Flag any that only rely on the ID being hard to guess.
2. Show what logout does. Confirm it clears the session token, auth cookies, localStorage and sessionStorage, and invalidates the token on the server.
Report as a table with file:line and a one-sentence fix, then stop.
```

Check by hand: open user A's record URL as user B, and paste a private URL after logging out. Neither should load.

### When things go wrong

- **The AI says the fonts are fixed but Google still loads.** A package or theme is pulling them in. Ask it to search node_modules and every CSS and config file for googleapis and gstatic and name the package.
- **Replay still shows typed text.** The dashboard setting overrides the code. Change it there and test again with a fake email.
- **You get a legal letter or demand.** Don't ignore it and don't reply yourself. Send it to a lawyer and fix the issue it describes straight away.

## Launch checklist

Run before any site or app goes live, and again after big changes. Mark each item passed, failed, N/A or UNSURE, with evidence. Labels: [Saved] from Stefano's saved reels; ⚠️ verify before relying on it.

### Pre-launch checklist [Saved]

From the @yatesvids and @buildwithfrancis reels.

#### Legal pages and business details
- [ ] Privacy policy page
- [ ] Terms and conditions page
- [ ] Cookies policy
- [ ] Refund policy, where something is sold
- [ ] Real business details
- [ ] Local laws checked (see the "Legal and compliance (UK, EU, Spain, US)" section)

#### Consent and data
- [ ] Cookie consent checked
- [ ] Form consent checked
- [ ] Only necessary data collected
- [ ] Tracking checked
- [ ] Third-party embeds checked

#### Content and claims
- [ ] Image copyright checked
- [ ] Fake reviews removed
- [ ] Unsupported claims removed
- [ ] Button labels are clear

#### Accessibility
- [ ] Colour contrast checked
- [ ] Alt text on images
- [ ] Forms work by keyboard
- [ ] Accessibility issues fixed
- [ ] H1 and heading structure correct ⚠️ label partly obscured in the source reel

Standard to pick, from a screenshot Stefano saved: WCAG AA (the default), WCAG AA plus colour-blind-safe charts, or WCAG AAA contrast for body text (7:1 instead of 4.5:1). Build to WCAG 2.2 AA unless the project says otherwise.

#### Search and sharing
- [ ] No vercel.app or preview domain
- [ ] Specific page titles
- [ ] Meta descriptions
- [ ] Custom favicon
- [ ] Open Graph image
- [ ] Canonical URLs
- [ ] Social previews work
- [ ] sitemap.xml

#### Design and user experience
- [ ] Custom 404 page
- [ ] Designed loading states ⚠️ label partly obscured in the source reel
- [ ] Useful error messages ⚠️ label partly obscured in the source reel
- [ ] Mobile layouts work
- [ ] Consistent UI spacing
- [ ] No dead buttons or links

#### Code and performance
- [ ] No console errors
- [ ] No leftover console.logs
- [ ] No exposed source maps
- [ ] No massive JS bundles

### The six legal holes [Saved]

From the "How to protect your vibe coded app from getting sued" guide and the @dr.erinjacques and @securedbycasco reels. Run the full audit prompt in the "Compliance audit prompts" section before every launch, not just the first.

- [ ] Fonts load from your own app, not Google or another font CDN
- [ ] Session replay masks every input and loads only after consent
- [ ] Consent banner has Accept and Reject buttons that are equally easy to click
- [ ] Sign-up has a neutral age screen if children could use it, with the minimum age set to 13 (UK or US only), 14 (Spain only) or 16 (several EU countries); anyone younger is blocked without storing their data; Children's Code applied for under-18s (UK)
- [ ] Marketing email has recorded opt-in consent (unticked box), or the soft opt-in for existing customers
- [ ] Every marketing email has a postal address and a working unsubscribe link; unsubscribes honoured within 10 business days
- [ ] Checkout shows price, frequency, auto-renewal and how to cancel next to the pay button
- [ ] Users can cancel online as easily as they signed up; consent records saved for every subscriber
- [ ] If users upload content: DMCA agent registered ($6, renew every three years), copyright page live, Report button on every piece of user content
- [ ] Privacy policy and terms linked in the footer and at sign-up
- [ ] User B can't open user A's record by URL, and a logged-out URL no longer loads (see the "Security" section)

### Domain setup [Saved]

From the @danielwelsh_routiq reel ("You bought the domain. Now what?"). About 10 minutes in total.

1. **Split the site and the app with subdomains.** `www.` for the marketing site and `app.` for the product, each one CNAME record (about a minute to add). Do it now: moving the app later breaks every link anyone has shared.
2. **Send email from two subdomains, never the root domain.** `mail.` for operations mail (sign-up verification, receipts, booking confirmations, password resets, "no-reply") and `news.` for marketing mail (campaigns, newsletters). If marketing mail gets flagged as spam, only `news.` suffers: resets from `mail.` still arrive and the main address on the root domain is untouched.
3. **Publish sitemap.xml and submit it in Google Search Console.** This is how search engines find every page.

Add for each sending subdomain [Practice]: SPF, DKIM and DMARC records from the email provider, and a working unsubscribe link on marketing mail.

### Final sign-off

- [ ] Every applicable item has been checked, with evidence where possible.
- [ ] Legal pages match what the site or app actually does.
- [ ] A real browser check confirms no non-essential tracker fires before consent.
- [ ] Automated accessibility scan and manual keyboard and screen reader test completed. Automated tools alone are not enough.
- [ ] All ⚠️ items relevant to this project have been verified.
- [ ] Any remaining gaps have been reported plainly.

## App stores (Apple and Google)

[Researched] on 3 November 2026. ⚠️ Store rules change often: check the current guidelines before each submission.

### Apple App Store
- [ ] If the app allows account creation, offer account deletion within the app (Guideline 5.1.1(v)).
- [ ] Provide an accurate privacy policy and privacy label, including what third-party SDKs collect.
- [ ] Declare trader status for EU distribution under the Digital Services Act. Apps without it have been removed from EU App Stores.
- [ ] Check the current Review Guidelines, privacy manifest rules and age rating. ⚠️ Apple updates these often.

### Google Play
- [ ] Complete the Data safety form, including SDK data collection and the data deletion questions.
- [ ] If the app allows account creation, provide account deletion in the app and through a web link.
- [ ] New personal developer accounts need a closed test with at least 12 opted-in testers for 14 continuous days. ⚠️ Based on third-party guides. Organisation accounts are reported as exempt but need a D-U-N-S number.
- [ ] Complete developer verification. ⚠️ Reported as mandatory from September 2026, so check Play Console.

## Feature ideas (optional)

Source: a reel screenshot, "20 cool features Claude can add to your website in one afternoon" (creator's handle not visible). These are a menu, not defaults. Add one only when it serves the page's main job, and never all of them: each one is more to maintain and test.

| # | Feature | Good fit | Watch out for |
|---|---|---|---|
| 1 | Dark mode toggle | Reading-heavy sites, apps used at night | Follow the system setting by default; check contrast in both themes |
| 2 | Language switcher | Real translated content (for example English, Spanish, Catalan) | Never machine-translate legal pages without review; set `lang` and `hreflang` |
| 3 | Back to top button | Long pages | Don't let it cover the main action; must be keyboard reachable |
| 4 | Reading progress bar | Long articles | Decorative, so hide it from screen readers |
| 5 | Copy button | Code, links, discount codes, emails | Confirm the copy ("Copied") |
| 6 | Save for later | Articles, products, resources | Storing it on the device may need consent unless the user asked for it ⚠️ check PECR |
| 7 | Recently viewed pages | Shops, docs | As above for storage |
| 8 | Keyboard shortcuts | Tools used daily | Never animate keyboard actions; show a shortcut list |
| 9 | Adjustable text size | Reading-heavy sites | The page must still work at 200% browser zoom anyway |
| 10 | Interactive tables | Data, comparisons, pricing | Keep comparisons short (UX audit item 37) |
| 11 | Searchable FAQs | Support, pricing, services | Make "no results" helpful (item 100) |
| 12 | Autosave forms | Long forms, drafts | Say that it saved; don't keep sensitive data on the device |
| 13 | Password visibility toggle | Any password field | Needs an accessible label |
| 14 | Share page buttons | Articles, events | Third-party share scripts can track: use plain links |
| 15 | Estimated reading time | Articles | Be honest: "6 min read" |
| 16 | Filter and sort options | Lists of more than about 10 items | Show the active filter and a way to clear it |
| 17 | Table of contents | Long guides and legal pages | Highlight the current section |
| 18 | Smart search bar | More than a few screens of content (item 90) | Accept typos; suggest results |
| 19 | Form success notification | Every form | Say what happens next (item 92, 52) |
| 20 | Offline access | Apps used on the move | Service workers cache data; plan updates and clearing |

UK rules in force since 5 February 2026 include an exception for remembering appearance preferences such as language or dark mode (the "Legal and compliance (UK, EU, Spain, US)" section).

## Companion skills and design references

These are other people's open-source skills. This standard keeps their key ideas in the "Design and craft" section and the "Motion and faux UI" section, so it works even when none of them is installed. Install one only when the task needs its depth or tooling.

⚠️ **Before installing any of them:** skills can run scripts on your machine. Impeccable downloads and runs a binary and can add an edit hook; Oil UI runs an update check. Read what a skill runs before you install it, and install per project rather than globally if unsure.

| Skill | Use it for | Install | Licence |
|---|---|---|---|
| [Impeccable](https://github.com/pbakaus/impeccable) (Paul Bakaus) | Full design workflow with commands: shape, critique, audit, polish, harden, typeset, layout, clarify and more. Includes a "slop" detector you can run on a folder or URL. | `npx impeccable install` (detects your tools). Claude Code: `/plugin marketplace add pbakaus/impeccable`. Scan only: `npx impeccable detect src/` | Apache 2.0 |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (Next Level Builder) | Searchable database: styles, palettes, font pairings, 119 UX rules, chart types and stack-specific advice. Good for picking a starting design system. | Claude Code: `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill` then `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill`. Others: `npm install -g ui-ux-pro-max-cli` then `uipro init --ai codex` (or `claude`, `gemini`) | MIT |
| [Emil Kowalski's skills](https://github.com/emilkowalski/skills) | Motion and polish: animate, review-animations, remove-animations, choreograph, apple-design, mobile-native, break-ui (worst-case data), pick-ui-library, prototype. | `npx skills@latest add emilkowalski/skills` | MIT |
| [Oil UI](https://github.com/oil-oil/oil-ui) | Design method: a one-line "north star", one hero and one main action per screen, greyscale structure before colour, review from real screenshots. Written in Chinese, but replies in your language. | `npx skills add oil-oil/oil-ui` | MIT (the free edition; it mentions a paid Pro version) |
| [Stageshow](https://benji.org/stageshow) (Benji Taylor) | Faux product UI: believable product screenshots and animated demos for landing pages and feature cards, with filming and checking scripts. | `npx skills add benjitaylor/skills --skill stageshow` | MIT |
| [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) (VoltAgent) | Not a skill: a library of 84 DESIGN.md files analysing real sites (Linear, Stripe, Notion and others). | Copy one DESIGN.md into a project as a reference | MIT |

### Which to reach for

- **New page, no design system yet:** write a DESIGN.md first (see the "Design and craft" section). UI UX Pro Max or Impeccable's `shape` and `init` can help draft it.
- **Reviewing an existing UI:** run the "UX audit (132 items)" section first; add `npx impeccable detect` for a mechanical pass.
- **Animation work:** Emil Kowalski's `animate`, `review-animations` or `remove-animations`.
- **Marketing demo or hero illustration of the product:** Stageshow.
- **Stress-testing a component:** Emil Kowalski's `break-ui`.

### Using awesome-design-md safely

DESIGN.md is a plain markdown design system file (colours, type, spacing, components, do's and don'ts) that agents read before building UI. The format comes from Google Stitch. Use the collection to learn how a good DESIGN.md is structured, or to borrow an interaction pattern. Do not ship a site that copies another company's look, name or marks: it can mislead users and infringe their rights. Always write your own DESIGN.md from your own brand.

## Sources

### Stefano's saved material
- "How to protect your vibe coded app from getting sued" guide (the six legal holes, with fix prompts), from the skool.com/raycfu community, saved as a text file with six sketch images (November 2026)
- Instagram reels: @yatesvids (pre-launch checklist), @buildwithfrancis (pre-launch issues), @securedbycasco (security prompt reaction; IDOR and logout tests), @dr.erinjacques (Google Fonts and the GDPR, with a self-hosting prompt), @haydenschmitty (four design patterns), @danielwelsh_routiq (domain setup), @charles.unemployed (20 AI design slop indicators; removing AI slop from an OTP screen), and a screenshot of "20 cool features Claude can add to your website in one afternoon" (creator not visible)
- UX audit prompt (132 items), saved as a text file
- Website and app build standards (UK and EU), version 3 November 2026
- Accessibility standard options, from a screenshot (September 2026)
- [Lincoln Devine: secure your vibe-coded app](https://lincolndevine.com/guides/secure/)

### Companion skills and references
- [Impeccable (Paul Bakaus)](https://github.com/pbakaus/impeccable)
- [UI UX Pro Max (Next Level Builder)](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [Emil Kowalski's skills](https://github.com/emilkowalski/skills)
- [Oil UI](https://github.com/oil-oil/oil-ui)
- [Stageshow (Benji Taylor)](https://benji.org/stageshow) and [repo](https://github.com/benjitaylor/skills)
- [awesome-design-md (VoltAgent)](https://github.com/VoltAgent/awesome-design-md)

### Where skills load (checked 4 November 2026)
- [Codex: build skills (OpenAI)](https://learn.chatgpt.com/docs/build-skills)
- [Gemini CLI: Agent Skills](https://geminicli.com/docs/cli/skills/)
- [Skills on Google Gemini (Hands-on AI, third party)](https://handsonai.info/platforms/google-gemini/skills/)


### UK
- [ICO: storage and access technologies, final guidance summary (Osborne Clarke)](https://marketinglaw.osborneclarke.com/advertising-regulation/new-exceptions-explained-in-ico-final-guidance-on-storage-and-access-technologies-could-online-advertising-be-next/)
- [PECR changes in force (Womble Bond Dickinson)](https://www.womblebonddickinson.com/uk/node/17075)
- [ICO's new guidance (ZwillGen)](https://www.zwillgen.com/eu-uk/ico-cookie-crackdown-2-icos-new-storage-access-technologies-guidance/)
- [UK cookie guidance and analytics (CookieYes, vendor)](https://www.cookieyes.com/blog/uk-cookie-guidance-ico-pecr/)
- [Company information on websites (Business Companion)](https://businesscompanion.info/node/604/printable/pdf)
- [Registered office note (Burges Salmon)](https://burges-salmon.com/-/media/files/non-pub-pdfs/registered_office_and_sail_addresses.pdf)
- [CMA208: fake reviews guidance](https://assets.publishing.service.gov.uk/media/67eeb64fe9c76fa33048c790/CMA208_-_Fake_reviews_guidance.pdf)
- [DMCC Act overview (LegalVision)](https://legalvision.co.uk/commercial-contracts/dmcc-act/)
- [DMCC compliance and subscriptions (Myerson)](https://www.myerson.co.uk/news-insights-and-events/compliance-for-online-businesses-under-the-dmcca)
- [UK accessibility approach (Taylor Wessing)](https://www.taylorwessing.com/en/interface/2022/the-european-accessibility-act/what-is-the-uks-approach-to-accessibility)
- [UK accessibility law (Scope)](https://business.scope.org.uk/uk-law-and-digital-accessibility-what-it-means-for-your-organisation/)
- [The Children's Code: background (ICO)](https://ico.org.uk/about-the-ico/what-we-do/background-to-the-children-s-code/)
- [ICO: direct marketing using electronic mail (updated 28 April 2026)](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/)
- [ICO guidance on opt-outs at collection (Mills and Reeve)](https://www.mills-reeve.com/blogs/charity/may-2026/electronic-marketing-rules-for-charities-clarified-in-new-ico-guidance/)
- [PECR regulation 22 and the charitable purposes soft opt-in (Osborne Clarke)](https://marketinglaw.osborneclarke.com/advertising-regulation/new-consent-free-marketing-route-for-charities-ico-publishes-guidance-on-the-charitable-purposes-soft-opt-in/)
- [ICO Reddit and Imgur decisions (Chambers)](https://chambers.com/articles/children-s-privacy-enforcement-intensifies-lessons-from-ico-s-reddit-and-imgur-decisions)

### EU and Spain
- [Withdrawal button (Hogan Lovells)](https://www.jdsupra.com/legalnews/eu-consumer-protection-law-update-new-9377759/)
- [Withdrawal button (K&L Gates)](https://www.klgates.com/thought-leadership/New-EU-Withdrawal-Button-Requirement-Practical-Implications-and-Recommendations-for-US-and-Global-Online-Sellers-7-8-2026)
- [Withdrawal button (Crowell)](https://www.crowell.com/en/insights/client-alerts/from-checkout-to-opt-out-the-eu-withdrawal-button-is-here-what-e-commerce-businesses-need-to-know)
- [European Accessibility Act microenterprise exemption (Accessible.org)](https://accessible.org/?p=12023334)
- [EAA and standards status (Shopappy)](https://shopappy.com/?p=12373)
- [Digital Omnibus status (Acompli)](https://acompli.ie/news/digital-omnibus-gdpr-cookies-status-september-2026/)
- [AI Omnibus and Article 50 (Dastra)](https://www.dastra.eu/en/blog/simpler-safer-stricter-where-it-counts-inside-the-eu-ai-omnibus-deal/60025)
- [AI Omnibus (Gibson Dunn)](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
- [AEPD cookie guide summary (ECIJA)](https://www.ecija.com/actualidad-insights/guia-aepd-uso-cookies/)
- [LSSI and cookies (Atico34)](https://protecciondatos-lopd.com/empresas/?p=36036)
- [AEPD legal report on LSSI Article 21 and tacit consent](https://www.aepd.es/es/documento/2018-0164.pdf)
- [AEPD resolution on LSSI Article 21 opt-out address](https://www.aepd.es/documento/a-00180-2014.pdf)
- [Business databases and LSSI Article 21 (Fieldfisher)](https://www.fieldfisher.com/es-es/locations/spain/insights/bases-datos-empresariales)
- [AEPD fines Nude Project €20,000 (Marketing4eCommerce)](https://marketing4ecommerce.net/multa-nude-project/)
- [GDPR Article 8 thresholds by country (GDPRLocal)](https://gdprlocal.com/dealing-with-childrens-data/)
- [GDPR Article 8 thresholds and legal bases (Privacy skills reference)](https://www.skills.lc/mukul975/Privacy-Data-Protection-Skills/mukul975-privacy-data-protection-skills-skills-privacy-managing-consent-for-children-skill-md)
- [Spain's age of consent and draft law (Linklaters)](https://www.linklaters.com/en/insights/data-protected/data-protected---spain)
- [EU Kids Act proposal and Spain's 14-year threshold (Osborne Clarke, October 2026)](https://www.osborneclarke.com/insights/eu-kids-acts-proposed-new-online-child-protection-rules-signal-legal-reforms-spain)

### US (checked 10 November 2026)
- [SB 690 signed: CIPA reform (WilmerHale)](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20261006-cipa-reform-signed-into-law)
- [SB 690 leaves §631 and §632 claims intact (Katten)](https://katten.com/california-partially-eliminates-california-invasion-of-privacy-act-claims-faced-by-many-companies)
- [SB 690 and the 1 January 2027 start (Usercentrics, vendor)](https://usercentrics.com/us/?p=20647)
- [FTC civil penalty amounts, 2025 adjustment (Federal Register)](https://www.federalregister.gov/documents/2025/01/17/2025-01361/adjustments-to-civil-penalty-amounts)
- [No 2026 FTC penalty adjustment (CO Consulting, secondary)](https://christopholivierconsulting.com/?p=9137)
- [California Automatic Renewal Law amendments (Cooley)](https://www.cooley.com/news/insight/2025/2025-06-04-california-automatic-renewal-law-amendments-take-effect-on-july-1-2025)
- [California ARL price change notice (Perkins Coie)](https://perkinscoie.com/print/pdf/node/9051)
- [DMCA designated agent FAQ (US Copyright Office)](https://copyright.gov/dmca-directory/faq.html)
- [DMCA agent rules and address note (Perkins Coie)](https://perkinscoie.com/print/pdf/node/3757)

### Design
- Claude's built-in frontend design skill (reviewed directly)
- [Scoring Show HN submissions for AI design patterns (Adrian Krebs)](https://www.adriankrebs.ch/blog/design-slop/)
- [How to fix AI slop in web design (Capital and Compute)](https://capitalandcompute.net/blog/fix-ai-slop-design/)
- [How to avoid the vibe-coded look (Robots on Payroll)](https://robotsonpayroll.substack.com/p/how-to-avoid-that-vibe-coded-look)

### Apps and coding
- [Apple: account deletion within apps](https://developer.apple.com/news/?id=mdkbobfo)
- [Google Play: account deletion requirements](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en-GB)
- [Apple EU trader status removals (TechCrunch)](https://techcrunch.com/2025/02/18/apple-purges-apps-without-contact-info-from-eu-app-store-as-dsa-deadline-hits)
- [Google Play closed testing (Choicely)](https://www.choicely.com/blog/google-play-12-tester-rule)
- [Google Play developer verification (Testers Community)](https://www.testerscommunity.com/blog/google-play-developer-verification-2026)
- [Vibe-coded app security failures (DEV Community)](https://dev.to/cypriantinasheaarons/the-vibe-code-teardown-why-your-app-can-pass-the-demo-and-still-fail-security-checks-2p7l)
- [Manual security checks (DEV Community)](https://dev.to/mafengpam/what-i-found-when-i-security-scanned-10-ai-built-apps-and-how-to-check-yours-manually-13a2)
