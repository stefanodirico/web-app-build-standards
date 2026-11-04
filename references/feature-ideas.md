# Feature ideas (optional)

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

UK rules in force since 5 February 2026 include an exception for remembering appearance preferences such as language or dark mode ([legal-and-compliance.md](legal-and-compliance.md)).
