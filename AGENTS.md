# BG3 Party Guide

## Scope

This repository contains two related local tools:

- The primary application is a single-user Baldur's Gate 3 party guide. A small
  Rust/Axum server serves `src/ui/index.html`, assembles guide data from
  `content/**/*.md`, and persists checklist state in `progress.json`.
- `bg3kb/` is an optional Python pipeline that scrapes bg3.wiki, cleans and
  chunks pages, builds a LanceDB hybrid-search index, and exposes CLI, daemon,
  and MCP search interfaces. It is not part of the web application's runtime.

Keep both tools' service interfaces local and loopback-only. Do not add remote
binding, authentication, TLS, multi-user behavior, or a frontend build system
unless the task explicitly requests that scope.

## Repository map

The tree divides four ways: **code**, **displayed data**, **raw resources**,
and **reasoning**. Put a new file in the bucket that matches what it *is*, not
what it is about.

- `src/`: all application source.
  - `src/main.rs`: Axum routes, loopback listener, static-file services, and
    graceful shutdown.
  - `src/content.rs`: YAML-frontmatter parser and `/api/plan` assembly.
  - `src/progress.rs`: mutex-protected, atomic persistence for `progress.json`.
  - `src/ui/index.html`: the complete vanilla HTML/CSS/JavaScript UI. There are
    no Node dependencies or generated frontend assets.
- `content/`: runtime guide content and the source of truth for guide data.
  This is the only content the web application displays.
- `resources/`: raw source material, gathered rather than authored. Nothing
  here is reasoning and nothing here is hand-maintained prose.
  - `resources/videos/transcripts/`, `resources/videos/summaries/`: expert
    video text.
  - `resources/reddit/`: scraped posts (`posts/`), `links.txt`, and
    `research.md`, the compiled digest of those posts.
  - `resources/wiki/`: per-class bg3.wiki extractions.
  - `resources/tiers/`: extracted tier datasets read by `tools/` —
    `item_tiers.json`, `spell_tiers.json`, `item_vocab.json`, and the
    per-video tables in `slots/` and `spells/`.
  - `resources/notes/`: loose pasted scratch text, safe to delete.
- `docs/`: reasoning — why the builds are what they are, which decisions were
  taken, and how the datasets are produced. Never displayed by the
  application.
- `tools/`: scripts that turn `resources/` into `content/`. They are run from
  the repository root and hardcode their paths relative to it.
- `progress.json`: git-tracked playthrough state, not fixture data.
- `bg3kb/`: separate Python knowledge-base implementation and its own README.
- `bg3kb/data/`: large scraped/chunked/indexed artifacts. Treat these as
  generated pipeline outputs even though many are tracked.

## Web application behavior

Run the binary from the repository root. It uses the current working directory
to find `content/`, `src/ui/index.html`, and `progress.json`.

The HTTP surface is:

- `GET /api/plan`: reload and assemble the Markdown content on every request.
- `GET /api/progress`: return the in-memory progress snapshot.
- `POST /api/progress`: apply `{ "key": "...", "checked": true|false }` and
  persist it.
- `/docs/*` and `/resources/*`: read-only static mounts, present so the
  header's companion-doc chips resolve.
- All other paths: static files rooted at `src/ui/`.

The repository root is deliberately not served. Keep the static roots explicit
and narrow when adding routes: `progress.json`, `bg3kb/`, and dotfiles must
stay off the HTTP surface.

The default address is `http://127.0.0.1:8787`; `BG3_PORT` changes only the
port. Preserve the `127.0.0.1` binding because the application deliberately has
no authentication.

## Content conventions

Treat `content/**/*.md` as authoritative. Content-only edits are hot-reloaded;
refreshing the browser is enough.

Every content file must begin with a `---` YAML frontmatter fence and include a
closing `---` fence. A leading BOM and CRLF are accepted. The Markdown body is
parsed but currently not rendered, so user-visible guide data belongs in the
frontmatter.

`content/meta.md` carries a `version` field, which `index.html` renders as the
version chip in the header. Bump it for every distinct set of changes — a minor
bump for a feature or a broad content sweep, a patch bump for a fix — so the chip
never claims a state the guide has moved past.

`src/content.rs` assembles exactly these top-level API fields:

- `meta` from `content/meta.md`
- `party` from `content/party.md`
- `proficiencies` from `content/proficiencies.md`
- `loot_guide` from the `loot_guide` field in `content/loot.md`
- `tadpole` from `content/tadpole.md`
- `characters` from every Markdown file in `content/characters/`
- `ratings` from the `ratings` field in `content/ratings.md`, and only when that
  file exists — it is generated, so a checkout that has not run the generator
  simply serves no `ratings` and the frontend hides the Ratings tab

Each character file requires a unique string `nickname` and a `builds` value.
Characters are ordered by `party.roster[].nickname`; characters absent from the
roster sort afterward by nickname. Preserve the existing schema and copy the
shape of a neighboring entry when adding data, because the frontend is the
schema consumer and there is no separate schema file.

A build may carry an `at_a_glance` object with three string fields — `armour`,
`elixir` and `concentration` — which `index.html` renders as a chip row at the
top of the build, ahead of the Playstyle card. It states the armour proficiency
the build actually has, the elixir it drinks every long rest, and what its
concentration is spent on. Keep each to one line and keep exactly those three
keys; the frontend renders nothing else from it.

For character itemization, prefer objects with stable `id`, display `item`,
`slot`, and explanatory `note`, `effect`, or `why`. Keep `id` stable when
renaming display text. The UI recognizes `act1`, `act2`, and `act3` specially
and renders other populated itemization keys afterward.

`item` (and a loot row's `name`) is the item's name and nothing else, because it
doubles as the bg3.wiki page title whenever `wiki` is absent. Anything else the
row wants to say belongs in the `note`, or in a field of its own:

- `held: 1|2|3` marks gear carried over from that act and renders as an "Act N"
  chip; `held: true` renders a bare "Held" when the act is not worth naming.
- `wiki:` overrides the page title when the display name legitimately differs
  ("Deathstalker Mantle" -> `The Deathstalker Mantle`), takes a list for a row
  that names two items, and takes `false` for a slot placeholder or a vendor
  rollup that is not an item at all.

Place `held` after `rank_note` and before `wiki`, which is where
`apply_item_tiers.py` leaves it; anywhere earlier and every regen reshuffles the
file. Do not single-quote a name just because it contains an apostrophe -- that
applier matches the raw line, so `'Melf''s First Staff'` stops resolving.

A `leveling` row separates what the class hands over from what the player
chooses, and each `recommendations` entry says which it is:

- `picks: N` -- how many selections that level opens for the category. When the
  entry names fewer than `N`, the frontend renders the remainder as explicit
  "open pick" placeholders, so a granted-but-unassigned choice stays visible
  instead of disappearing. Naming more than `N` is allowed and badges as
  "N picks · M listed" for a pick-one-of-these row.
- `granted: true` -- the class, subclass or race supplies this for free: no
  spell-known pick and no prepared slot. Add `fixed: true` when it is not even
  steerable, like a recruited companion's racial cantrip.
- `optional: true` -- the level-up replacement swap rather than a new pick.

For prepared casters the count is a capacity, not an increment, because the list
re-opens on every level and swaps freely out of combat: give the row that level's
whole prepared loadout with `picks` set to Paladin level + CHA modifier, and let
the unnamed remainder show as open slots. For known casters `picks` is the number
of new spells that level adds.

A `spells` entry may carry `source: granted` for the same distinction in the
spell panel, where it badges "Free" beside the `Lv N` guide badge. Only mark
spells the game actually hands over -- oath spells, a draconic ancestry spell, a
racial cantrip -- never an expanded spell list, which widens the options a pick
may choose from without granting anything.

An itemization entry, or one of its `options`, may also carry an external rating
from the guide corpus in `resources/videos/summaries/`:

- `tier` / `tier_note`: a letter tier (`S`, `A`, `B`, `C`, `D`, `F`) from that
  slot's tier list, plus the source video, timestamp and verdict.
- `rank` / `rank_note`: a placing such as `'#12'` (or `HM`) in that act's top-20
  countdown, plus the same provenance.

The two are independent and an item often holds both, which is the point: the
letter says how good it is inside its own slot, the number how it stands against
every item in the act.

These fields are generated. `resources/tiers/item_tiers.json` is the source of truth;
`tools/apply_item_tiers.py` writes it into the content and is idempotent, so edit
the dataset and re-run rather than hand-editing a rating. Only record a rating the
corpus actually states -- never convert a rank into a letter, and never carry a
rating over from a spell, feat, or class tier list.

An entry in a build's `spells` block carries the same `tier` / `tier_note` pair,
read from the spell and cantrip tier lists instead of the gear ones, and the Spells
panel badges every level card the same way it badges itemization. A spell never
carries `rank`, because that series runs no top-20 countdown. The source of truth is
`resources/tiers/spell_tiers.json` and the applier is `tools/apply_spell_tiers.py`.

The two appliers own different regions of the same files: `apply_spell_tiers.py` only
touches lines inside a `spells:` block and `apply_item_tiers.py` only touches lines
outside it. Keep that split if you change either one — both strip their managed fields
wholesale before rewriting, so a widened region silently deletes the other's ratings.
Entries that the spell series does not rate (class features such as Extra Attack, which
share the `- spell:` shape) stay unbadged; the applier reports any entry with a real
spell level that it could not match.

## Guide ratings

`resources/tiers/item_tiers.json` and `resources/tiers/spell_tiers.json` hold every rating read out
of the tier-list corpus — 823 item ratings across 35 lists and 212 spell ratings across
11. They are the source of truth for the `tier`/`rank` fields in the content, and are
regenerated, not hand-edited:

```sh
python tools/fetch_transcripts.py <playlist>     # transcripts
python tools/dump_tier_verdicts.py --source <id> # verdicts, in order, with context
python tools/merge_slot_tiers.py                 # resources/tiers/slots/*.json  -> item_tiers
python tools/merge_spell_tiers.py                # resources/tiers/spells/*.json -> spell_tiers
python tools/apply_item_tiers.py                 # dataset -> content/characters/*.md
python tools/apply_spell_tiers.py                # dataset -> the spells blocks
python tools/build_ratings_page.py               # dataset -> content/ratings.md
```

The last three write the places a rating surfaces, and all are overwritten wholesale
on every run: `apply_item_tiers.py` badges the party's own gear on the character pages,
`apply_spell_tiers.py` badges the spells and cantrips in each build, and
`build_ratings_page.py` writes the Ratings tab, which shows every rated item in the
corpus rather than only the party's. Re-run the relevant ones after a merge; never
hand-edit `content/ratings.md`.

Read `docs/extraction-brief.md` before touching any of it. Attributing a spoken
verdict to the right item is the whole difficulty, and the brief records the failure
modes that cost accuracy: the narrator introduces the *next* item immediately after a
verdict, the captions mangle the word "tier" a dozen different ways, one verdict can
rate several items, and later lists revise earlier ones. Automated attribution was
tried and rejected — it scored 7 right, 0 wrong, 22 missed against known answers.

Both mergers report anything that needs a human look: an item rated differently by two
lists, a file whose rated-plus-unassigned count does not reconcile with the verdicts it
saw, and any rating a complete re-read has corrected.

## Progress compatibility

`progress.json` has the stable shape:

```json
{
  "version": 1,
  "checked": {}
}
```

Only checked entries are stored, in sorted key order. Unchecking removes a key.
Writes use `progress.json.tmp` followed by an atomic rename and roll back the
in-memory update on failure.

Do not reset, normalize, or use the real `progress.json` as test scratch.
Preserve `version` and existing keys. Checklist keys are minted in
`index.html` from slugs and stable IDs:

- `lvl:<character>/<build>/<segment>/<level>`
- `item:<character>/<build>/<act>/<item-id>`
- `loot:<act>/<area>/<item-name>`

Changing a character nickname, build name, leveling segment label, loot area,
or loot item name can orphan existing checkoffs. Itemization display names may
change safely when their explicit `id` remains unchanged.

A character page and the Loot tab list the same gear, so their two keys are
linked and a single tick writes both. `index.html` builds the link groups at
boot by normalising item names — parentheticals, a leading "The", possessive
`'s`, and everything after the first item of a combined row are all dropped —
and only links a group that has a member on each side. The key shapes above are
unchanged; linking is a runtime map, not a stored field, so it needs no
migration and a name that matches nothing simply stays independent. Groups
inherited from before linking are completed in memory at boot and are not
written back; the next real toggle persists the whole group.

## Frontend conventions

Keep `index.html` dependency-free and consistent with its DOM-helper/render
function style. The UI intentionally includes accessible ARIA tabs, keyboard
navigation, focus management after view changes, hover/focus item tooltips, and
light/dark theme persistence. Preserve those behaviors when changing
navigation or rendering.

Switching sub-views rebuilds the whole page, so each view key remembers its
scroll offset and the selected tab in each of its tab groups, and restores them
on return. That state lives in `sessionStorage` under `bg3-view-state-v1` and is
disposable. Scroll recording is parked while a view is swapped in, and focus is
moved with `preventScroll` so the restored offset survives; keep both if you
touch `renderContent`, and keep tab-group `idBase` values stable per view or
remembered tabs will not be found again.

The frontend tolerates some legacy scalar/list shapes with `arr()` and `has()`,
but new content should use the current structured shapes. Keep progress writes
optimistic with rollback on failed POSTs.

Top-level tabs are built from a list passed into `buildTopTabs`, so a tab whose
data is absent is never rendered; Ratings is the one that works this way. The
Ratings views are pure reference — no checkboxes, no progress keys — and the
generator has already sorted each act's items, so `ratingTierGroups` only breaks
the run where the letter changes rather than re-deriving an order of its own.

## Rust commands and validation

```sh
cargo fmt --all -- --check
cargo test
cargo check
cargo run                 # http://127.0.0.1:8787
cargo run --release
```

Use the smallest relevant validation, then expand based on the change:

- Rust changes: run formatting, tests, and `cargo check`.
- Content changes: with the server running, confirm `GET /api/plan` returns
  successfully, refresh the browser, and inspect the affected view.
- UI changes: exercise the affected view in a browser, including keyboard tab
  behavior, focus, tooltips, theme, and a narrow viewport when relevant.
- Progress changes: run `cargo test`; use a disposable working directory for
  manual POST tests so the real playthrough state is not mutated.

The project was originally pinned for Rust 1.82 compatibility. Do not update
the lockfile's `indexmap`/`hashbrown` compatibility pins or upgrade
dependencies as incidental cleanup; read the development note in `README.md`
before an intentional toolchain upgrade.

## Knowledge-base conventions

Follow `bg3kb/README.md` for setup and run order. The intended environment is a
`uv`-managed virtual environment created under `bg3kb/.venv`; embedding and
search may require a CUDA-enabled PyTorch install and a cached Hugging Face
model.

The pipeline is:

```text
scrape -> clean -> chunk -> embed/index -> CLI, daemon, or MCP search
```

Keep shared knobs and paths in `bg3kb/config.py`. Before a real scrape, replace
the placeholder `USER_AGENT` contact, retain the polite rate limit/maxlag/retry
behavior, and preserve resumable atomic cache writes. Scraped content is CC
BY-SA 4.0; keep source URLs in derived chunks for attribution.

Do not rebuild or commit thousands of files under `bg3kb/data/` for unrelated
Python edits. `embed_index` overwrites the LanceDB table, `--rechunk` rebuilds
`chunks.jsonl`, one-shot CLI calls may start a loopback daemon on port 8765, and
model/index operations can be slow and GPU-heavy. Validate the narrowest
affected stage first, for example:

```sh
python -m bg3kb.clean "Bhaalist Armour"
python -m bg3kb.chunk "Bhaalist Armour"
python -m bg3kb.cli "where do I find Bhaalist Armour" --k 5
```

There is currently no dedicated Python test suite. Avoid using a full scrape or
index rebuild as a routine validation step.

## Change discipline

- Preserve unrelated working-tree changes; this repository is often used with
  content, UI, and generated-data edits in progress together.
- Keep changes scoped to the owning subsystem and avoid editing generated or
  research artifacts unless the task calls for them.
- Update `README.md` or `bg3kb/README.md` when commands, configuration, or
  architecture change in a way users need to know.
