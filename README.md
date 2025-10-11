# community (personalized)

Voice command set for [Talon](https://talonvoice.com/), customized for simplified, accuracy-focused grammar.

For agent guidance and summary of differences from upstream, see:
- AGENT_GUIDE.md  
- docs/CHANGES_FROM_UPSTREAM.md

## AI Agent Working Notes

- Primary focus: improve Talon grammar accuracy and ergonomics for this personalized setup.
- Key entry points:
  - `core/keys/keys.py`, `core/keys/keys.talon`, `core/keys/keystroke.talon`
  - `core/keys/*.talon-list` (letter, special, modifier, number, arrow, keypad)
  - `core/keys/symbols.py`
  - `core/modes/*.talon`, `core/modes/modes.py`
  - `settings.talon`, `settings/*.csv`
- Guidance:
  - Preserve current spoken forms; propose alternates rather than replacements.
  - Favor `.talon-list` → captures in `.py` → grammar in `.talon` separation.
  - Prefer `edit.*`/`user.*` actions over hardcoded chords where applicable.
  - Keep contexts narrow to reduce active vocabulary.
  - Avoid reintroducing removed upstream features without explicit instruction.
- Read `AGENT_GUIDE.md` and `docs/CHANGES_FROM_UPSTREAM.md` before large changes.

## Core Components

### Alphabet
Custom alphabet defined in [letter.talon-list](core/keys/letter.talon-list): ach, bik, kaj, ..., zed.
Say `help alphabet` to display the alphabet.

### Keys and Symbols
- Key commands: [keys.talon](core/keys/keys.talon)
- Symbols: [symbols.py](core/keys/symbols.py) - simplified short forms (tick, bang, lace, race)
- Special keys: [special_key.talon-list](core/keys/special_key.talon-list) (boot=backspace, jet=space, etc.)
- Modifiers: [modifier_key.talon-list](core/keys/modifier_key.talon-list) (shi=shift, etc.)

### Formatters
Available via `help format`. Chain formatters like `snake hello world` → "hello_world".
Defined in [formatters.py](core/formatters/formatters.py).

### Modes
- Command/dictation modes: [core/modes/](core/modes/)
- Custom sleep/wake: `snore` to sleep, `welcome back` to wake
- Mixed mode available for command+dictation together

### Editing Commands
Global editing commands in [edit.talon](core/edit/edit.talon):
- `undo that`, `redo that`
- `paste that`, `copy that`, `cut that`
- `go word left`, etc.

### Window Management
Commands in [window_management.talon](core/windows_and_tabs/window_management.talon):
- `running list` - show app switcher
- `focus chrome` - focus applications

## Settings
Configurable via [settings.talon](settings.talon). Key settings:
- `imgui.scale` - UI scaling
- `user.help_max_command_lines_per_page` - help display
- Mouse scroll amounts

## Customization
- Lists: `.talon-list` files for vocabulary
- CSV files in `settings/` folder
- Voice commands: `customize` + list name (abbreviations, alphabet, etc.)

## File Structure
- `core/` - Core Talon functionality
- `plugin/` - Additional plugins (minimal)
- `settings/` - Configuration files
- `docs/` - Documentation
