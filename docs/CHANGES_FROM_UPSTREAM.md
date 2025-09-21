## Summary of key differences from talonhub/community

This fork is streamlined for personal grammar and accuracy. Highlights below are based on a diff with the upstream repository at the time of writing.

### Keys and symbols

- Alphabet (`core/keys/letter.talon-list`): Replaced upstream default with a custom set: ach, bik, kaj, …, zed. Do not revert.
- Symbols (`core/keys/symbols.py`): Simplified, short spoken forms (e.g., tick, bang, lace, race) and trimmed currency to dollar only.
- Special and modifier keys moved/defined in lists:
  - `core/keys/special_key.talon-list` includes backspace=boot, space=jet, delete=dij, enter=slap, etc.
  - `core/keys/modifier_key.talon-list` defines Mac-focused modifiers with `shi` for shift.
- `core/keys/keys.talon`: Added explicit passthrough rules for `<user.number_key>` and `<user.arrow_key>`.
- `core/keys/keystroke.talon`: Local file providing numeric-repeat commands for arrows, words, and keys, plus mapped editing actions (`edit.copy()`, etc.).

### Modes and wake/sleep

- `core/modes/command_and_dictation_mode.talon`: Added `mixed mode` to enable command+dictation together.
- `core/modes/modes_not_dragon.talon`: Custom sleep/wake phrasing; `snore` forms for sleep; avoids Dragon-specific phrases.
- `core/modes/sleep_mode.talon`: Custom wake phrase `welcome back` with wake sequence.
- Several upstream mode files (deep sleep, dragon mode, language modes) are not present locally.

### Numbers

- Upstream split of prefixed/unprefixed numbers not present; local behavior is defined under `core/numbers/` and reused in keystroke repeats.

### Settings

- `settings.talon`: Many upstream defaults are commented/disabled to reduce mouse/GUI features; double pop timing customized.

### General philosophy changes

- Prefer concise, unique spoken forms to reduce ambiguity.
- Use `.talon-list` to define vocabulary; use captures in `keys.py` to compose grammar; keep actions in Python.
- Prefer `edit.*`/`user.*` actions over hardcoded chords, except where deliberate.

If you need the precise upstream line-by-line diff for a file, fetch upstream and compare only the target file(s) before proposing changes.


