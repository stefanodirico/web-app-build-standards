# UX audit (132 items)

Source: a saved UX audit prompt. Transcribed in full; only spelling was changed to British English (colour, centred, postcode) and headings to sentence case.

## Rules for running it

Work read-only: do not edit, install, delete, commit or deploy anything until the user approves the fixes at the end. Reading files and read-only commands (ls, grep, git log) are fine.

### Step 1. Map the app

Say in a few lines: the framework, where routes or screens are defined, the component library or design system, and where shared styles or theme tokens live. Then list the main screens (home or landing, sign up and onboarding, the core feature screens, pricing, checkout, settings) with the file each one lives in. If there are more than 15, pick the 15 people use most and say which were skipped.

### Step 2. Check every screen against every item

Read the actual components and styles, not just file names, and follow imports into shared components (Button, Input, Nav, Layout) to judge what actually renders. Note the file and line each answer is based on. If an item doesn't apply to a screen (no form, no pricing), mark it N/A and move on.

### Step 3. Report back in this order

a) One table: Priority | Screen | Item # | What's wrong | Evidence | Suggested fix. Evidence is file:line. The fix is one line. List only items that fail or are UNSURE, sorted HIGH first, and name the screens that passed everything in one line under the table.

b) Priority: HIGH if it slows down or blocks the main action on a key screen (sign up, onboarding, checkout, the core feature) or locks someone out (accessibility); MEDIUM if it adds friction somewhere else; LOW if it's polish.

c) Things that can't be judged from code (real tap sizes on a phone, real load times, contrast on images, how a screen feels): list them as MANUAL, with how to check each one.

Never say an item passes without evidence; if it can't be told from the code, say UNSURE and why. No generic advice: every row points to a real file in the repo.

Then stop and ask which fixes to make. Change no file until the user says yes. When they do, fix them one at a time and show each diff.

## Part 1: UX laws

### Hick's law
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

### Fitts's law
The smaller a button is and the further away it is, the longer it takes to tap, and every miss is another chance for someone to give up.
11. Make the main button big. Big enough to tap without looking.
12. Put it at the bottom of the screen. Where the thumb is already sitting.
13. Make the whole list row tappable. Not just the text or a small icon.
14. Keep delete far away from save. A missed tap shouldn't destroy anything.
15. Most-tapped means biggest and easiest to reach. Size and position should follow how often it's used.

### Jakob's law
People spend most of their time in other apps, so they expect yours to work the same way. When it doesn't, it feels broken.
16. Logo top left, and it goes home. Tapping it should always take people to the start.
17. Cart and profile top right. That's where people look for them.
18. Use icons people already know. Like a magnifying glass for search.
19. Use the words people expect. A sign in button just says "Sign in".
20. Save your creativity for what only you do. Keep the basics standard.

### The Von Restorff effect
The one thing that looks different is the thing people notice. When everything stands out, nothing does.
21. Make one thing on each screen look different. Different from everything else on it.
22. Make it different in one way. Like the colour or the size.
23. Keep everything around it plain. So it has something to stand out against.
24. Use it on the button that matters most. The one you most want people to press.
25. Highlight less. Every extra highlight makes the first one stand out less.

### The goal-gradient effect
People speed up as they get close to the finish line, and if the finish line is hidden, they give up.
26. Show how many steps are left. From the very first step.
27. Start the progress bar a little full. So it feels like they've already started.
28. Make the last step the easiest one. Don't save the hard question for the end.
29. Put progress next to the button. Right beside the button they need to press.
30. Show the next goal straight away. The second they finish one, show how close the next one is.

### The Doherty threshold
If your app responds in under 400 milliseconds, people stay focused. Any slower and their attention starts to drift.
31. Every tap does something right away. Even if it's just the button pressing down.
32. Show the change now, save it in the background. Don't make the screen wait for the server.
33. Start anything slow early. While they're still busy doing something else.
34. Show a grey outline while a page loads. A skeleton of the page, not a spinner.
35. Show a progress bar for anything slow. So people know it's still working.

## Part 2: More laws and principles

### Miller's law
People can only hold a handful of things in their head at once. Miller put it at about seven; later research puts it lower.
36. Don't make people remember things between screens. Show the code, the price or the earlier choice again where it's needed.
37. Keep side-by-side comparisons short. A 20-row comparison table is a memory test.
38. Don't treat "seven" as a menu rule. It's about memory, not a magic number of menu items.

### Chunking
Grouping small pieces into bigger, meaningful units makes them easier to read and remember.
39. Format long numbers in groups. Phone numbers, card numbers and codes: 4242 4242, not 42424242.
40. Break long text into short sections. With headings people can skim.
41. Split long lists into labelled groups. Ten settings in three groups beat ten in a row.

### Cognitive load
Every bit of thinking your interface asks for uses up attention people would rather spend on what they came to do.
42. Cut anything that doesn't help the task. Decorations, extra links, repeated text.
43. Let people pick instead of remember. Show options to choose from rather than a blank box.
44. Do the maths for them. Show totals, dates and conversions already worked out.

### The serial position effect
People remember the first and last items in a list best, and the middle ones least.
45. Put the most important items first and last. In nav bars, menus and feature lists.
46. Don't bury key actions in the middle. Of a long menu or a long page.
47. Open and close with what should stick. Your main benefit up top, your call to action at the end.

### The Zeigarnik effect
People remember unfinished tasks better than finished ones, so a visibly incomplete task pulls them back.
48. Show what's left to do. A setup checklist with the unticked items showing.
49. Save progress automatically. So leaving never means starting over.
50. Bring people back to where they stopped. Resume, don't restart.

### The peak-end rule
People judge an experience mostly by its most intense moment and by how it ended, not by the average.
51. Make your best moment great. Usually the first time the product actually works for them.
52. End every flow on a high note. A clear, friendly success screen after sign up or checkout.
53. Give the worst moments extra care. Errors, failed payments and cancelling.

### Tesler's law
Every task has some complexity that can't be removed. The only question is whether the app handles it or the user does.
54. Let the app carry the complexity. Detect the country, format the phone number, fill the city from the postcode.
55. Don't simplify by removing what people need. Hiding a needed option just moves the work to them.
56. Pre-fill everything you already know. Name, email, last-used settings.

### Postel's law
Be strict in what you send and flexible in what you accept. It started as a rule for internet protocols and works just as well for forms.
57. Accept input in any sensible format. Phone numbers with or without spaces, dashes or brackets.
58. Clean input up instead of rejecting it. Trim stray spaces, ignore capital letters in emails.
59. Be consistent in what you show back. One date format and one currency format everywhere.

### The aesthetic-usability effect
People see good-looking designs as easier to use, and forgive small problems in them.
60. Polish the screens people see first. Landing, sign up and the first screen after it.
61. Keep spacing, colour and type consistent. Small inconsistencies read as "unfinished".
62. Watch what testers do, not what they say. A pretty screen can hide real problems.

### The law of proximity
Things that are close together look like they belong together.
63. Put each label right next to its field. Closer to its own field than to the one above.
64. More space between groups than inside them. Spacing is how people see the groups.
65. Keep a button next to what it acts on. Not at the far end of the screen.

### The law of similarity
Things that look alike seem to work alike.
66. Style everything clickable the same way. One look for links, one for buttons.
67. Don't style plain text like a link. Or a label like a button.
68. One colour, one meaning. If red means delete, don't also use it for "new".

### The law of common region
Things inside the same border or background read as one group.
69. Use cards or panels to group related things. One card per item, one panel per topic.
70. Don't box things that aren't related. A shared box says "these go together".
71. Keep a section's actions inside its box. So it's clear what the button affects.

## Part 3: Checklists

### Onboarding
72. Let people try it before signing up, where you can. Show the product working before asking for an email.
73. Ask only for what you need to start. Everything else can wait.
74. Get people to a first useful result fast. Count the taps from sign up to "oh, nice".
75. Teach by doing, not with a slideshow. Hints on the real screen beat a five-slide tour.
76. Let people skip optional steps. And finish them later.

### Forms and input
77. Use one column. Fields side by side are easy to miss.
78. Labels above fields, not just placeholders. Placeholder text disappears the moment people type.
79. Bring up the right keyboard. Email, number and phone fields get the matching keyboard on mobile.
80. Support autofill and password managers. Set the right autocomplete attributes.
81. Check a field when people leave it. Not on every keystroke, and not only on submit.

### Buttons and CTAs
82. Say what happens on the button. "Create account", not "Submit".
83. Start with a verb. Save, Send, Start free trial.
84. Stop double taps. Show a loading state and disable the button while it works.
85. Make buttons look like buttons. And links look like links.
86. Confirm only what can't be undone. Offer undo instead of "Are you sure?" on everything.

### Navigation
87. Show where people are. Highlight the current tab or page.
88. Keep navigation in the same place everywhere. It shouldn't move between screens.
89. Make back always work. Browser back and swipe back shouldn't lose people's work.
90. Make search easy to find. If there's more than a few screens of content.
91. Use clear labels, not clever ones. "Pricing", not "Plans & Possibilities".

### Feedback, loading and speed
92. Confirm every action. A checkmark, a toast or a changed state.
93. Offer undo for things people might regret. Archive, delete, send.
94. Stop the layout jumping as it loads. Reserve space for images and late content.
95. Say what's happening during long waits. "Uploading 3 of 10" beats a spinner.
96. Test speed on a mid-range phone. On a slow connection, not just your laptop on wifi.

### Empty states
97. Never show a blank screen. Explain what will appear here.
98. Give one clear action to fill it. "Create your first project".
99. Offer an example or template. So people aren't starting from nothing.
100. Make "no results" helpful. Suggest a spelling fix, a wider filter or something related.
101. Treat "all done" as good news. An empty inbox should feel like a win.

### Errors
102. Say what went wrong in plain words. Never just an error code.
103. Say how to fix it. "Use at least 8 characters", not "Invalid password".
104. Show the error next to the field. Not only in a banner at the top.
105. Keep what people typed. One error should never wipe a form.
106. Prevent errors before they happen. Date pickers, input limits, clear formats.

### Mobile and thumb reach
107. Put main actions in easy thumb reach. The lower part of the screen.
108. Space tap targets apart. So people don't hit the one next to it.
109. Don't rely on hover. There's no hover on a touchscreen.
110. Don't hide key actions behind gestures only. Swipe-to-delete needs a visible option too.
111. Test it one-handed on a real phone. Not just in a desktop browser.

### Accessibility
112. Text contrast of at least 4.5:1. 3:1 for large text (WCAG AA).
113. Tap targets of at least 44x44 points. Apple's guideline. Android's is 48x48 dp.
114. A visible focus state. Never remove the focus outline without a replacement.
115. Alt text on meaningful images. And empty alt text on decorative ones.
116. Respect reduced motion. Turn off big animations when the system setting asks.
117. Never use colour alone to carry meaning. Add an icon or text to red and green.

### Typography and readability
118. Body text at least 16px on mobile. Smaller text gets skipped or zoomed.
119. Keep lines to roughly 50-75 characters. Long lines are hard to follow.
120. Line height around 1.5 for body text. Tight paragraphs are tiring.
121. One clear heading hierarchy. Each level clearly smaller than the last.
122. Left-align body text. Centred paragraphs are hard to read.

### Copy and microcopy
123. Write the way you talk. Plain words, short sentences.
124. Say what it does for them. The outcome, then the feature.
125. One word for one thing. Don't call it a "project" here and a "workspace" there.
126. Cut every word that doesn't help. Then read it out loud.
127. Be specific. "Takes 2 minutes", not "quick and easy".

### Trust and pricing pages
128. Show the real price up front. Including fees, before the last step.
129. Say what happens after the trial. When they'll be charged, and how much.
130. Make cancelling as easy as signing up. No hunting through settings.
131. Use real proof only. Real reviews, logos and numbers. Never made-up ones.
132. Make contact and refund info easy to find. A visible email or help link, not a maze.
