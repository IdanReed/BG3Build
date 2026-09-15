# UI style guide

The visual specification for `src/ui/index.html`. Every CSS rule and every
render function that emits a visual element follows this document. When the
two disagree, fix the code or amend this file in the same change.

Decisions recorded here were taken on 2026-09-14 and are not open for
re-litigation inside an implementation task. Propose changes as a separate
edit to this file.

## 1. Intent

The guide is a reference document the player reads at the table. It should
look like a well-typeset Markdown file: monospace, black ink on paper, rules
and whitespace for structure, no decoration. It must read the same printed as
on screen, and it must never look like a dashboard.

Three goals, in priority order:

1. **Minimal, brutalist.** Structure comes from type weight, case, rules, and
   indentation. Nothing is drawn that does not carry information.
2. **Plain Markdown, but better.** The vocabulary is Markdown's: bold headings,
   dashed bullets, `[ ]` / `[x]` checkboxes, ruled tables. The layout is what a
   good renderer would do with it, not what a text editor shows.
3. **Static.** The page could be printed and lose nothing but the checkboxes'
   click. No motion, no floating chrome, no hover-only structure.

References: [The Monospace Web](https://owickstrom.github.io/the-monospace-web/)
for grid-aware monospace layout, and GitHub's rendered Markdown for the shapes
of headings, lists, and tables.

## 2. Banned

These do not appear anywhere in the stylesheet or in JS-emitted markup.

- `border-radius` other than `0`.
- `box-shadow`, `text-shadow`, gradients, `backdrop-filter`, `filter`.
- `transition`, `animation`, `transform` used for motion.
- Emoji, and any glyph outside the font's own repertoire.
- Pill or capsule shapes. Badges are bracketed text.
- Filled colour backgrounds on badges, rows, chips, or hover states. Colour is
  applied to text and to borders only.
- `letter-spacing`. Monospace is already spaced.
- `opacity` for de-emphasis. Use `--muted`.
- `color-mix()`. Every colour is a named token.
- Inline `style` attributes in JS-emitted markup.
- Sticky or fixed elements other than the sidebar nav and the tooltip.
- A second surface colour. There is paper and there is ink.

## 3. Typography

One family, two weights, one size for almost everything.

| Token      | Value                                                        | Use                                   |
| ---------- | ------------------------------------------------------------ | ------------------------------------- |
| `--font`   | `"JetBrains Mono", ui-monospace, "Cascadia Mono", Consolas, monospace` | everything                  |
| `--fs`     | `16px`                                                       | body, tables, nav, headings           |
| `--fs-sm`  | `13px`                                                       | meta lines, badges, table headers, labels |
| `--fs-lg`  | `20px`                                                       | page title only                       |
| `--lh`     | `1.5rem` (24px)                                              | the vertical unit                     |

- Weights are 400 and 700. Nothing else. No italics; the one current italic
  (empty slot placeholder) becomes muted text.
- Body line height is `--lh`. Small text uses `line-height: 1.5` and is not
  forced onto the grid.
- Headings do not grow. A section heading is body size, bold, uppercase. Only
  the page title uses `--fs-lg`.
- `text-transform: uppercase` is allowed only on: section headings, table
  header cells, nav group headings, slot labels, and small key labels
  (`ARMOUR`, `ELIXIR`). Never on body text or item names.
- Numbers in tables use `font-variant-numeric: tabular-nums` (a no-op in mono,
  kept for the system fallback).

### Font files

JetBrains Mono, SIL Open Font License 1.1. Ship the two static weights from
the official release, plus the licence:

```text
src/ui/fonts/JetBrainsMono-Regular.woff2
src/ui/fonts/JetBrainsMono-Bold.woff2
src/ui/fonts/OFL.txt
```

Declared with `font-display: swap`. The static-file route already serves
`src/ui/`, so no server change is needed. Two files rather than one because the
official release does not ship a variable woff2; together they are 187 KB.

## 4. Colour

Two themes, one palette inverted. Colour is applied to text and borders, never
as a fill. Every text colour meets WCAG 4.5:1 against `--bg` in its theme.

| Token       | Light (paper) | Dark      | Use                                              |
| ----------- | ------------- | --------- | ------------------------------------------------ |
| `--bg`      | `#f7f6f2`     | `#151514` | page, tooltip, everything behind text            |
| `--ink`     | `#1a1a1a`     | `#e8e6e0` | text                                             |
| `--muted`   | `#5c5c5c`     | `#9c9a93` | secondary text, inactive tabs, labels, checked rows |
| `--rule`    | `#c8c6c0`     | `#3b3a37` | all borders and rules                            |
| `--accent`  | `#1f4e9c`     | `#8ab0ea` | links, current nav item, active tab, checked box, focus ring, rank |
| `--warn`    | `#a04b00`     | `#f0a860` | warn callout label, `verify` flag, D tier        |
| `--tier-s`  | `#8a6400`     | `#e0b04a` | S tier letter and box                            |
| `--tier-a`  | `#1f7a3c`     | `#6cc48a` | A tier                                           |
| `--tier-b`  | `#2f5fb3`     | `#86aaf0` | B tier                                           |

- C tier uses `--muted`. D tier uses `--warn`. Rank (`#12`) uses `--accent`.
- `--good` is removed. Granted picks are marked with text, not green.
- Theme selection: `html[data-theme]` set before first paint, toggle in the
  header, `localStorage` key `bg3-theme`, `prefers-color-scheme` fallback.
  All existing behaviour, unchanged.

## 5. Spacing and measure

Vertical spacing is in line units. Horizontal spacing is in characters.

| Token        | Value     | Use                                     |
| ------------ | --------- | --------------------------------------- |
| `--lh`       | `1.5rem`  | one line; margin between blocks         |
| `--lh-half`  | `.75rem`  | inside a component                      |
| `--measure`  | `110ch`   | content column maximum                  |
| `--prose`    | `80ch`    | paragraph maximum inside the column     |
| `--nav-w`    | `26ch`    | sidebar width                           |
| `--gutter`   | `4ch`     | between sidebar and content, page edges |

- Block margins are `--lh` between sections and `--lh-half` inside them.
  No other vertical values.
- Horizontal padding is `1ch` or `2ch`. Table cells use `1ch` vertical
  `.25rem`.
- Content wider than `--measure` (the leveling table, the proficiency matrix)
  scrolls horizontally inside a wrapper with no border. It does not reflow the
  column.

## 6. Layout

```text
BG3 Party Plan  v2.3         Mode: Honour · Patch 8 · research · goals   [dark]
Party   Loot   Locations   Ratings
────────────────────────────────────────────────────────────────────────────────
PARTY             │ Charles
  Overview        │ Vengeance Paladin 6 / Fiend Warlock 6
  Proficiencies   │
CHARACTERS        │ Contents: Playstyle · Overview · Ability scores · Leveling
> Charles         │
  Fiend Vengeance │ ARMOUR heavy   ELIXIR Bloodlust   CONCENTRATION Hold Person
  Asterion        │
  Gloom Assassin  │ PLAYSTYLE
  Gale            │ ───────────────────────────────────────────────────────────
  Bonbon          │ Open with Hold Person, then ...
```

- **Header.** Not sticky. One line: title (bold), version (muted), then
  `Mode`, `Patch`, and companion-doc links as a muted `·`-separated run, then
  the theme toggle at the right edge. The assumptions `<details>` stays, muted,
  on its own line. Below it the top tabs, then a full-width rule.
- **Top tabs.** A row of text buttons separated by three spaces. Active is
  bold and `--accent` with a 2px `--accent` underline. Inactive is `--muted`.
  Hover is `--ink`. ARIA tablist behaviour is unchanged.
- **Grid.** Two columns: `--nav-w` and `minmax(0, var(--measure))`, gap
  `--gutter`, centred. The sidebar has a `1px --rule` right border that runs
  the full height of the content.
- **Sidebar.** `position: sticky; top: 0`. Plain text. Group headings are
  `--fs-sm` bold uppercase `--muted`. Items are body size. The current item is
  bold `--accent` and prefixed `> ` via `::before`; others are prefixed two
  spaces so text aligns. A sub-label (build name, act, region) sits on the
  next line, `--fs-sm --muted`. No backgrounds, no dots.
- **Content.** Page title (`--fs-lg` bold), subtitle (`--muted`), a
  `Contents:` line, then sections. The sticky outline bar is removed; the
  `Contents:` line is a static `·`-separated list of anchor links to the
  page's sections and replaces `addPageOutline`'s observer entirely.
- **Section.** Heading (bold uppercase) with a `1px --rule` bottom border,
  then body. Sections are separated by `--lh`. No box, no background.
- **Prose.** Paragraphs cap at `--prose`. Lists use a real `-` marker via
  `::before` with a `2ch` hanging indent.
- **Breakpoints.** Below `60rem` the sidebar becomes a wrapped text row above
  the content and loses its border and stickiness, and the leveling table
  stacks each level as a block. Below `40rem` the ability grid drops to two
  columns and the facts grid to one. Itemization columns are `auto-fit`, so
  they need no breakpoint.

## 7. Components

Old element on the left, new treatment on the right. Class names stay where
the DOM shape survives; only removed concepts are renamed.

| Current                               | New                                                                                      |
| ------------------------------------- | ---------------------------------------------------------------------------------------- |
| `.card`                               | `<section class="sec">`: heading with bottom rule, no box                                 |
| `.chip`, `.chips.glance`              | `.glance`: a two-column `key   value` grid capped at `--prose`; key `--fs-sm` uppercase `--muted`, value body text |
| `.app-version`                        | Plain `v2.3` in `--muted` after the title                                                |
| `.badge`, `.pick-badge`, `.spell-plan-badge` | Bracketed token `[2 picks]`, `[free]`, `[swap]` in `--fs-sm --muted`, no border  |
| `.open-pick`                          | `[ open ]` in `--muted`                                                                  |
| `.item-tier` letter                   | `[S]` : one letter in brackets, text and brackets in the tier colour, bold               |
| `.item-tier.tier-rank`                | `#12` in `--accent`, bold, no brackets                                                   |
| `.item-chip` (held)                   | `(Act 1)` or `(held)` in `--fs-sm --muted`                                               |
| `.item-bis` star                      | `*` before the name in `--accent`, bold; the 3px left bar is removed                     |
| `.card-icon`, slot/class/category icons | Removed. `cardIcon`, `classIcon`, `levelCategoryIcon`, `ITEM_SLOT_ICONS` are deleted    |
| `.card-count`                         | ` (3)` after the heading text in `--muted`                                               |
| `.item-slot`                          | Subsection: `HEAD` label line (`--fs-sm` bold uppercase), rows beneath, `--lh-half` below |
| `.item-rows` (3 columns)              | Three columns of subsections at full measure, via `auto-fit` at `30ch` minimum, so the count drops on its own as the window narrows. No rule between column groups |
| `.level-number`                       | Right-aligned number, bold                                                               |
| `.level-table` columns                | Width hints on the cells: level `4ch`, class `18ch`, gains `28ch`; picks take the rest. Without them one long class string starves the other columns and the table overflows |
| `.level-choice`                       | One line: category in a fixed `12ch` column (`--fs-sm` uppercase `--muted`), then the pick in bold, then `[?]` when it has detail. No box |
| `.level-choice.is-grant`              | Same line, `[free]` token after the pick                                                 |
| `.level-legend`                       | One `--fs-sm --muted` line: `[2 picks] selections this level opens   [free] granted by the class   [ open ] not yet chosen` |
| `.detail-cue`                         | `[?]` in `--muted`; hover or focus opens the tooltip                                     |
| `.facts` dl                           | Two-column `key   value` grid, key `--fs-sm` uppercase `--muted`, `12ch` wide            |
| `.statblock`, `.ability-card`         | Six columns, each `STR` label over the final value in bold, growth chain beneath as `8 → 16 (+2 ASI)` lines in `--muted` |
| `.meter`                              | Text bar: `████████░░░░ 8/12` using `█` and `░`, bar in `--ink`, remainder in `--rule`    |
| `.tag`, `.tag-list`                   | Comma-separated inline text, bold                                                        |
| `.callout`                            | `NOTE` or `WARN` label (`--fs-sm` bold uppercase) then body, whole block has a `2px` left border in `--rule`; warn label in `--warn` |
| `.tabs`, `.tab` (sub-tabs)            | Text row `Act 1 · Act 2 · Act 3`; active bold `--accent` underlined, inactive `--muted`  |
| `.table-wrap`, `table`                | No outer border. Header cells `--fs-sm` bold uppercase `--muted` with a `1px --rule` bottom border. Rows separated by `1px --rule`. No zebra, no hover |
| `tr.total-row`, `tr.loot-core`        | Bold text; `loot-core` also gets the `*` prefix. No fill                                 |
| `.who-chip`                           | Plain text                                                                               |
| `.ck` checkbox                        | Native input kept for a11y, visually replaced by `[ ]` / `[x]` in the label. Checked: `x` in `--accent`; the row text turns `--muted`. Focus draws the ring around the brackets |
| `ul.clean li::before` dot             | Removed; rows are unmarked or use `-`                                                    |
| `.item-name` dotted underline         | `1px dotted --rule` underline kept; hover turns it `--accent`                           |
| `a.wiki-item::after ↗`                | Kept. `↗` is in the font                                                                 |
| `.item-tip`                           | `position: fixed` kept. `1px solid --ink` border, `--bg` fill, no radius, no shadow, no fade. Label `--fs-sm` uppercase `--muted`; facts as a `key   value` grid |
| `.theme-toggle`                       | Text button `[dark]` / `[light]`, `--muted`, hover `--ink`                               |
| `.rate-tier-h`                        | Section heading with the `[S]` letter first                                              |
| `li.rate-row` left bar                | Removed; rows separated by `--lh-half`                                                   |
| `.prof-table` cells                   | `P` `E` `H` `–` letters: expertise bold `--accent`, proficient `--ink`, half `--muted`, none `--rule` |
| Route and location markup (`.route-step`, `.curse-chip`, `.loc-link`, `.route-warn`, `.route-leave`, `.pc-*`) | In flight on `main` as uncommitted work, not in this branch's base. Once merged: step number in a `4ch` column, title bold, `do` prose beneath, `WARN` line in `--warn`, `Then` in `--muted`; `curse-chip` becomes `(no curse)` / `(torchlight)` / `(deep curse)` text; `loc-link` is styled as a link |
| `.skip-link`                          | Kept, `--accent` text on `--bg` with a `1px --ink` border when focused                   |

### Interactive states

- **Focus.** `outline: 2px solid var(--accent); outline-offset: 2px` on every
  focusable element. Never removed, never rounded.
- **Hover.** Text colour only: `--muted` to `--ink`, or `--ink` to `--accent`
  on links. No background, no border change, no shadow.
- **Current / active / checked.** `--accent` plus bold. This is the one
  emphasis the accent carries, so it is never used decoratively.
- **Disabled or empty.** `--muted`. Never `opacity`.

### Tooltips

Hover and focus behaviour is unchanged: `attachHoverTip`, `positionItemTip`,
pinning, and dismissal all stay. Only the box changes. Width stays
`min(390px, calc(100vw - 32px))`.

## 8. Print

```css
@media print
```

- Hide: header controls (theme toggle, skip link), sidebar, top tabs, sub-tab
  rows, `[?]` cues, `↗` markers.
- Show every sub-tab panel stacked, each preceded by its tab label as a
  `--fs-sm` uppercase heading. This needs each panel to carry
  `data-tab-label`, set in `miniTabs` and the build tab builder. It is the one
  behavioural addition in this restyle.
- Checkboxes print as `[ ]` / `[x]` because they are text.
- Force `--bg: #fff` and `--ink: #000`. Tier colours stay; they are legible in
  greyscale by letter anyway.
- `a[href^="http"]::after { content: " (" attr(href) ")" }` is **not** used.
  Wiki links are recognisable by name.

## 9. Stylesheet structure

One `<style>` block. The trailing block after `</script>` is merged into it.
Order, each under a `/* ---- Name ---- */` comment:

1. Tokens (`:root`, `html[data-theme="dark"]`, `@media (prefers-color-scheme: dark)` fallback)
2. `@font-face`
3. Reset and base type
4. Header and top tabs
5. Layout grid, sidebar, content
6. Sections, headings, prose, lists
7. Tables
8. Checklist and checkbox
9. Badges: tier, rank, token, held
10. Tooltip
11. Leveling
12. Itemization
13. Ability scores
14. Spells
15. Loot
16. Proficiencies
17. Ratings
18. Locations and route
19. Callouts, meters, misc
20. Responsive
21. Print

Every rule uses tokens. A hex value outside section 1 is a defect.

## 10. JS touchpoints

The restyle is CSS-first, but these render functions emit visual decisions
and must change:

- `cardIcon`, `classIcon`, `levelCategoryIcon`, `itemSlotIcon`,
  `ITEM_SLOT_ICONS`: deleted, along with every call site. `cardHeading` takes
  `(title, count)`.
- `renderHeader`: chips become a text run; `📄` is removed; `.app-version`
  becomes a span after the title.
- `buildThemeToggle`: label text `[dark]` / `[light]`; `title` unchanged.
- `addPageOutline`: replaced by `addContentsLine(wrap, sections)`, which
  returns a static `p.contents` of anchor links. The `IntersectionObserver`
  and `PAGE_OUTLINE_OBSERVERS` go.
- `checkbox`: wraps the input in a `label.ck-wrap` whose `::before` draws
  `[ ]` / `[x]` from `:checked`. `registerCheckbox` / `syncCheckboxNodes`
  unchanged.
- `pickBadge`, `itemTier`, `itemRank`, `itemHeldChip`, `curseChip`: text
  content gains its brackets or parentheses in JS so the glyphs are
  selectable and print.
- `renderBuild` glance row, `renderScores` meters, `renderTags`: new markup as
  described in section 7.
- `renderProficiencies`: marks are the letters `E`, `P`, `H` and `-`; the
  legend and note text in `content/proficiencies.md` say the same.
- `miniTabs` and the build tab group: set `data-tab-label` on each panel.
- Inline `style:` attributes in `renderBuild` and elsewhere: removed, replaced
  by classes.

Everything in `AGENTS.md` under *Frontend conventions* still holds:
tab-group `idBase` values, `sessionStorage` view state, scroll restore, focus
management, optimistic progress writes. Progress key shapes are untouched.

## 11. Acceptance

Before the branch merges:

- Every top tab and every sidebar entry renders with no console error.
- Keyboard: top tabs, sub-tabs, sidebar, checkboxes, `[?]` cues, wiki links
  all reachable and operable; focus ring visible on each.
- Tooltips open on hover and on focus, pin on click, dismiss on Escape.
- Theme toggle flips and persists across reload; dark palette passes 4.5:1
  spot checks on body, muted, accent, and each tier colour.
- Narrow viewport at `40rem` and `60rem`: no horizontal page scroll; wide
  tables scroll inside their wrapper.
- Print preview of a character page shows all acts stacked, no nav, no
  toggle, checkboxes legible.
- `grep -c 'border-radius\|box-shadow\|transition\|color-mix\|letter-spacing'`
  on the stylesheet returns `0` (allowing `border-radius: 0` if any).
- `grep -c 'style: "'` on the script returns `0`.
- `progress.json` untouched; `cargo check` and `cargo test` pass.
- `content/meta.md` version gets a minor bump.
- `AGENTS.md` *Frontend conventions* gains one line pointing here.
