# CLAUDE.md

Personalized fork of [talonhub/community](https://github.com/talonhub/community) — a voice command set for [Talon](https://talonvoice.com/). Streamlined for accuracy and a smaller active vocabulary. Primary user runs Windows (hostname `LenovoHG`); a Mac config (`Elhams-MacBook-Pro`) is also present.

**Goal of agent work in this repo:** improve grammar accuracy and ergonomics. Do not reintroduce upstream complexity that has been deliberately removed.

## Three-layer file philosophy

Talon separates **what you say** from **what it does**. Respect this split — it's the single most important convention here. See [philosophy.md](philosophy.md) for the long-form explanation.

| Layer        | Files            | Role                                                              |
| ------------ | ---------------- | ----------------------------------------------------------------- |
| Vocabulary   | `*.talon-list`   | Spoken word → string value. No grammar, no actions.               |
| Captures/Actions | `*.py`       | Reusable grammar components and Python action implementations.    |
| Grammar      | `*.talon`        | Voice commands that combine captures and call actions.            |

**Rule of thumb:**
- Adding a new word/phrase variant → edit a `.talon-list`.
- Adding a new command pattern → edit a `.talon` file, prefer reusing existing captures (`<user.modifiers>`, `<user.unmodified_key>`, `<number_small>`, etc.).
- Adding new behavior → add a Python action in a `.py` file, then call it from `.talon`.

## Default entry points

When asked to change keys/letters/symbols/modes, look here first:

- Keys: [core/keys/keys.py](core/keys/keys.py), [core/keys/keys.talon](core/keys/keys.talon), [core/keys/keystroke.talon](core/keys/keystroke.talon)
- Cross-OS vocab: [core/keys/letter.talon-list](core/keys/letter.talon-list), [core/keys/arrow_key.talon-list](core/keys/arrow_key.talon-list), [core/keys/number_key.talon-list](core/keys/number_key.talon-list), [core/keys/function_key.talon-list](core/keys/function_key.talon-list), [core/keys/keypad_key.talon-list](core/keys/keypad_key.talon-list)
- Per-OS vocab (mac/win split, mirrors upstream):
  - Mac: [core/keys/mac/modifier_key.talon-list](core/keys/mac/modifier_key.talon-list), [core/keys/mac/special_key.talon-list](core/keys/mac/special_key.talon-list)
  - Win/Linux: [core/keys/win/modifier_key.talon-list](core/keys/win/modifier_key.talon-list), [core/keys/win/special_key.talon-list](core/keys/win/special_key.talon-list)
- Symbols: [core/keys/symbols.py](core/keys/symbols.py)
- Modes / sleep / wake: [core/modes/](core/modes/)
- Edit actions per OS: [core/edit/edit_win.py](core/edit/edit_win.py), [core/edit/edit_mac.py](core/edit/edit_mac.py)
- Settings: [settings.talon](settings.talon), [settings/](settings/) (CSVs)

## Customizations from upstream (current state)

- **Alphabet** ([core/keys/letter.talon-list](core/keys/letter.talon-list)): custom phonetic set — `arch, bat, cage, drum, each, fine, gust, harp, ice, jury, crunch, look, mim, near, orange, pink, quench, red, sun, trap, urge, vest, wick, plex, yank, zip`. Do **not** revert to upstream NATO-style alphabet.
- **Symbols** ([core/keys/symbols.py](core/keys/symbols.py)): concise short forms (e.g. `bang`, `star`, `hash`, `amper`, `slash`); currency trimmed to `$` and `£`.
- **Modes / sleep**:
  - [core/modes/modes_not_dragon.talon](core/modes/modes_not_dragon.talon): `snore` to sleep (anchored, allows trailing phrase), `snore all` also hides UI overlays.
  - [core/modes/sleep_mode.talon](core/modes/sleep_mode.talon): wake phrase is `welcome back`.
  - [core/modes/command_and_dictation_mode.talon](core/modes/command_and_dictation_mode.talon): adds `mixed mode` to enable command + dictation simultaneously.
- **Keystroke repeats** ([core/keys/keystroke.talon](core/keys/keystroke.talon)): numeric-prefixed repeats like `<number_small> wipe → bksp:N`, `<number_small> up → up:N`, `<number_small> slap → enter:N`. Prefer extending these patterns over adding one-off rules. Cross-OS commands use `edit.*` actions (e.g. `duplicate <number_small>` uses `edit.paste(); repeat(N-1)` rather than a Mac-only `cmd-v` chord).
- **Settings** ([settings.talon](settings.talon)): mouse / GUI features mostly commented out (physical mouse in use); `speech.timeout = 0.6`; `imgui.scale = 1.3`; double-pop window 0.1–0.3s.
- Several upstream files removed: deep sleep, dragon mode, language modes, etc. Don't reintroduce without an explicit ask.

## Per-OS key vocabulary

Modifier and special keys are split per-OS to mirror upstream's structure (and because the spoken-form → key mapping differs between Mac and Windows). The matchers are disjoint, so exactly one file is active per OS — no merging.

- **Mac** (`os: mac`) — [core/keys/mac/modifier_key.talon-list](core/keys/mac/modifier_key.talon-list), [core/keys/mac/special_key.talon-list](core/keys/mac/special_key.talon-list). `super`/`command` → `cmd`; `function`/`globe` → `fn`. Special keys include `return: return` and `enter: keypad_enter` (Mac has both keys).
- **Windows / Linux** (`os: windows` + `os: linux`) — [core/keys/win/modifier_key.talon-list](core/keys/win/modifier_key.talon-list), [core/keys/win/special_key.talon-list](core/keys/win/special_key.talon-list). `super` → `super` (Windows key); `command` → `ctrl` so `command s` saves cross-platform. Adds `menu key` and `print screen`.
- **User-grammar invariants across both OSes**: `slap` → enter (primary), `wipe` → backspace, `delete` → forward-delete (not backspace), `backspace` → backspace.

When adding a key spoken-form that exists on both platforms, edit **both** files. When the key is OS-specific (e.g. `globe`/`menu key`), edit only the relevant file.

## Upstream reference

The canonical upstream repository is permanently cloned (read-only reference) at:

```
C:\Users\hamou\Documents\talonhub-community
```

Remote: `https://github.com/talonhub/community`

**Before starting a session** that will touch structural files (new commands, key vocab, captures, mode files), pull upstream to make sure it's current:

```bash
cd "C:/Users/hamou/Documents/talonhub-community" && git pull
```

**When to consult upstream before proposing changes:**
- Adding or restructuring a `.talon-list` — check if upstream uses a different file name, OS split, or header pattern.
- Adding a new capture or action — check if upstream already defines it under a compatible name.
- Adding an OS-specific file — verify upstream's `mac/` vs `win/` subdirectory convention for that file type.
- Unsure about a Talon key name — upstream's `*.talon-list` files are the fastest reference.

Compare only the specific file(s) relevant to the task. Do not wholesale-sync to upstream; this fork intentionally diverges in alphabet, symbols, sleep/wake, and removed features.

## Working guidance

- **Preserve current spoken forms.** Propose alternates rather than replacements. If renaming, update every dependent grammar file.
- **Prefer `edit.*` / `user.*` actions over hardcoded key chords**, except where the chord is intentionally OS-specific.
- **Keep contexts narrow.** Tighter `.talon` headers (os/app/tag/mode) shrink the active grammar and improve recognition. This is the main accuracy lever — Talon has no notion of weights or priorities.
- **Avoid spoken-form conflicts** within a `.talon-list` and across captures composed into `<user.unmodified_key>` (letters, numbers, symbols, arrows, special, function, keypad).
- **Don't reintroduce removed upstream features** (deep sleep, dragon mode, language modes, etc.) unless asked.
- For accuracy improvements: prefer `homophones.csv`-style substitutions and additional `.talon-list` entries over restructuring grammar.

## Layout

```
core/
  keys/        alphabet, symbols, captures, keystroke repeats
    mac/       modifier_key.talon-list, special_key.talon-list (os: mac)
    win/       modifier_key.talon-list, special_key.talon-list (os: windows + linux)
  modes/       command/dictation/sleep/mixed mode definitions
  edit/        per-OS implementations of edit.* actions
  numbers/     number capture (number_small, etc.)
  formatters/  snake/camel/title/etc. text formatters
  app_switcher/ window focus + app name overrides
  windows_and_tabs/  window/tab management
  ...
settings.talon       global settings + tag enables
settings/            user-customizable CSVs
conversation/        Q&A notes, voice cheatsheets (PDF + MD)
docs/                CHANGES_FROM_UPSTREAM.md, INSTALLATION_GUIDE.md
philosophy.md        long-form explanation of the three-layer split
plugin/              minimal plugin set (mostly upstream-trimmed)
private/             gitignored — sensitive bits (contacts etc.)
```

## Reference docs in this repo

- [philosophy.md](philosophy.md) — three-layer file model with worked examples (uses the older `ach`/`bik` alphabet in didactic prose; treat as historical, not authoritative).
- [docs/CHANGES_FROM_UPSTREAM.md](docs/CHANGES_FROM_UPSTREAM.md) — diff narrative vs upstream.
- [docs/INSTALLATION_GUIDE.md](docs/INSTALLATION_GUIDE.md) — setup notes.
- [BREAKING_CHANGES.txt](BREAKING_CHANGES.txt) — upstream breaking-change log (rarely relevant to local edits).
- [README.md](README.md) — mostly upstream README; user-facing rather than agent-facing.
- [AGENTS.md](AGENTS.md), [AGENT_GUIDE.md](AGENT_GUIDE.md), [.cursor/rules/01-agent.md](.cursor/rules/01-agent.md) — older Cursor-era notes; this CLAUDE.md supersedes them.

## Change workflow

1. **Pull upstream** (`cd "C:/Users/hamou/Documents/talonhub-community" && git pull`) if the task touches structural files — captures, key vocab, mode files, or new commands. Check the relevant upstream file(s) for naming conventions and OS split patterns before proposing anything.
2. Read the current state of the file(s) you're touching — don't trust the docs above for spoken forms.
3. Make granular edits. Prefer adding over renaming.
4. Verify no duplicate spoken forms in `.talon-list`s and that captures still parse.
5. Match indentation and style of the surrounding file.
6. If the change affects Mac vs Windows behavior, say so explicitly in the response.
