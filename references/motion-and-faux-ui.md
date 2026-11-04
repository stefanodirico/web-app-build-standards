# Motion and faux UI

[Distilled] from Emil Kowalski's skills (motion) and Benji Taylor's Stageshow (faux product UI). For depth, install them (see [companion-skills.md](companion-skills.md)).

## Should it animate at all?

| How often people see it | Decision |
|---|---|
| 100+ times a day (keyboard shortcuts, command menu) | No animation |
| Tens of times a day (hover, list navigation) | Remove or reduce a lot |
| Occasionally (modals, drawers, toasts) | Standard animation |
| Rarely (onboarding, celebrations) | Room for delight |

Every animation needs a reason: spatial consistency, showing a change of state, explaining something, feedback on a press, or avoiding a jarring jump. "It looks cool" is not a reason for something seen often. Never animate keyboard-triggered actions.

## Timing and easing

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

## Review checklist

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

## Faux product UI for marketing pages (Stageshow)

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
