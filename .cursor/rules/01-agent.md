## Cursor agent working notes

- Primary focus: improve Talon grammar accuracy and ergonomics for this personalized setup.
- Default entry points:
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


