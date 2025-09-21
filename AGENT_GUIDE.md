## Purpose

This repository is a personalized Talon user configuration focused on accuracy and simplified grammar. The agent’s primary goal is to improve recognition reliability and ergonomics without reintroducing upstream complexity.

## High-level architecture

- Core voice building blocks live in `core/keys` and `core/numbers`.
- Grammar is defined in `.talon` files; vocabulary in `.talon-list` files; reusable captures/actions in `.py` files.
- Modes and behavior gates are in `core/modes`.
- Project-wide settings are in `settings.talon` and CSVs under `settings/`.

## Key conventions (customized)

- Alphabet: `core/keys/letter.talon-list` uses a non-standard phonetic set (e.g., "ach"→a, "bik"→b). Do not replace with upstream alphabet.
- Symbols: `core/keys/symbols.py` defines concise spoken forms (e.g., "tick", "bang", "lace"). Maintain these mappings and extend via the same structure.
- Special keys and modifiers: Moved to `.talon-list` (`special_key.talon-list`, `modifier_key.talon-list`) to enable generic captures in `keys.py` and flexible combos like `<user.modifiers> <user.unmodified_key>`.
- Keystroke utilities: `core/keys/keystroke.talon` contains repeated-arrow/word and repeatable keypress patterns (e.g., `<number_small> boot: key("bksp:{number_small}")`). Prefer these over one-off hardcoded rules.
- Mixed mode: `core/modes/command_and_dictation_mode.talon` includes a `mixed mode` command that enables command+dictation together.
- Sleep/wake: Custom wake phrase `welcome back` in `core/modes/sleep_mode.talon`. Sleep is mapped to concise forms like `snore` in `modes_not_dragon.talon`.

## What to optimize

- Accuracy-first grammar: Minimize active vocabulary per context; prefer list-driven captures; avoid ambiguous homophones in high-traffic captures.
- Portability: Use editor/OS-agnostic actions (e.g., `edit.copy()`) instead of hardcoded key chords, unless a command is inherently chord-specific.
- Maintainability: Keep vocabulary in `.talon-list`, grammar in `.talon`, and logic/captures in `.py`. Do not mix concerns.

## Where to look by default

- Keys and grammar:
  - `core/keys/keys.py`, `core/keys/keys.talon`, `core/keys/keystroke.talon`
  - `core/keys/*.talon-list` (alphabet, special, modifiers, numbers, arrows, keypad)
  - `core/keys/symbols.py`
- Modes:
  - `core/modes/*.talon`, `core/modes/modes.py`
- Numbers:
  - `core/numbers/*`
- Settings and vocab tweaks:
  - `settings.talon`, `settings/*.csv`

## Constraints and preferences

- Keep my existing spoken forms; propose additions as non-conflicting alternatives.
- Favor short, distinct pronunciations for common primitives (letters, symbols, special keys).
- Do not reintroduce large upstream files/features I removed unless specifically requested.
- Any refactor should preserve current spoken forms unless explicitly changing them is the task.

## Examples of acceptable improvements

- Add safe alternates to `letter.talon-list` for letters with occasional misrecognition, ensuring no conflicts.
- Extend `symbols.py` with additional concise forms following the same `Symbol` structure.
- Replace hardcoded key chords in `.talon` files with corresponding `edit.*` or `user.*` actions where available.
- Tighten contexts in `.talon` headers (OS/app/tags) to reduce active grammar.

## Anti-goals

- Don’t migrate back to upstream’s default alphabet or symbol phrasing.
- Don’t add broad global commands that increase ambiguity without a gating context.

## Change workflow

1. Propose granular edits to the relevant file(s) above.
2. Ensure no conflicts in `.talon-list` (duplicate spoken forms) and captures still parse.
3. Prefer adding over renaming; if renaming, update all dependent grammar.
4. Keep indentation and style consistent with existing files.


