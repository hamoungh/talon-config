|### Improving command recognition accuracy (Conformer D2 + Talon)

This document proposes changes you can make in your Talon profile to improve recognition accuracy for command-style phrases and non-English letter names. It is based on your current repo layout and grammar:

- **Alphabet**: `core/keys/letter.talon-list` (e.g., `jack: j`, `kaj: c`, `ish|esh: e`, `queue: q`, `you: u`, `ex: x`, `wise: y`, etc.)
- **Key grammar**: `core/keys/keys.talon` and `core/keys/keys.py` (captures `{user.letter}`, `{user.letters}`, `{user.symbol_key}`, `{user.number_key}`, `{user.function_key}`, `{user.special_key}`, `{user.keypad_key}`)
- **Modes**: `core/modes/command_and_dictation_mode.talon`, `core/modes/dictation_mode.talon`, `core/modes/modes_not_dragon.talon`
- **Vocabulary**: `core/vocabulary/vocabulary.talon-list` and `settings/words_to_replace.csv`
- **Settings**: `settings.talon`

 make spoken forms more phonetically distinct, and avoid collisions.

---


## 2) Audit and improve the alphabet spoken forms

Your current letter names include many sibilants and near-minimal pairs that are hard for Conformer, especially in fast sequences:

- Examples of risky similarity: `ish` vs `esh`; `ach` vs `kaj`; sibilant endings like `-sh`, `-ch`, `-j` clustered together; English collisions like `queue` (q), `you` (u), `ex` (x), `wise` (y).

Recommendations:

- **Prefer high-contrast forms** with unique onsets and vowels. Avoid clusters of sibilant endings.
- **Avoid real English words** for letters you enter in command-mode: e.g., replace `queue` (q) and `you` (u) with non-words like `qunno`/`cuek` and `yule`/`uku` (examples—pick what’s natural for you).
\- **Remove near-duplicates**: pick either `ish` or `esh` for `e`, not both, unless you really need the alias; fewer options reduce ambiguity.
- **Add only the alternates you actually need**: too many variants per letter increases confusion.

Where to change:

- `core/keys/letter.talon-list`



---

## 3) Add a short unique prefix for letter sequences (optional)

use a short prefix that primes the recognizer for letters only for the next utterance:

- Example phrases: `spell …`, `letters …`, `chars …`
- Internally, gate a minimal context off that prefix so only `<user.letters>` (and maybe `<user.number_key>`) can match that utterance.

Benefit: Keeps normal command mode intact while giving you a high-precision path for rapid letter runs.

---

## 4) Trim command grammar breadth in command mode

Even in command mode, you currently expose many captures simultaneously:

- `{user.symbol_key}`, `{user.special_key}`, `{user.function_key}`, `{user.keypad_key}`, `{user.number_key}`, plus letter sequences and modifier combinations.

Recommendations:

- **Split keys grammar by tag**: only enable rarely used areas (e.g., keypad, function keys, obscure symbols) when needed.
- **Disable prose/vocabulary captures** while in command-only workflows if you aren’t using mixed mode.
- **Restrict “press <user.keys>”** if it conflicts with your letter usage—keep the focused commands you actually use.

Where to change:

- Split `core/keys/keys.talon` into multiple contexts gated by tags, then enable tags only as needed per application/context.

---

## 5) Tune speech segmentation for spelling

In `settings.talon`:

- Consider adjusting `speech.timeout` from the default 0.3s. A slightly higher value (e.g., 0.4–0.6) can help Conformer aggregate a rapid series of letters into a single utterance, improving stability of `<user.letters>`. If it feels laggy, step it back down.
- If you find the engine cutting you off mid-sequence, a longer timeout usually helps; if it’s lumping unrelated commands together, shorten it.

Note: This is highly personal—test with a few realistic coding sessions.

---

## 6) Eliminate specific collisions

Potential conflicts in your profile:

- `vocabulary.talon-list` includes custom entries like `kaaj` and `esnore`. While vocabulary mostly affects dictation, avoid overlapping with uncommon command words if you also use mixed mode.
- Sleep commands in `core/modes/modes_not_dragon.talon` expose `(esnore|snore)`; if “esnore” collides with any custom words you use, rename one side.

What to do:

- Keep odd vocabulary words out of mixed/command contexts (or rename them) if they overlap with your custom command lexicon.

---

## 7) Provide targeted aliases for your most-missed commands

Instead of adding many alternates for all letters, add **two or three carefully chosen alternates** only for the letters/commands you regularly miss. Make these alternates phonetically distant from both the original and other letters.

Where to change:

- Add a small number of extra lines under the same written letter in `core/keys/letter.talon-list` (multiple spoken forms can map to the same output letter).

---

## 8) Context-driven enablement by app

Use `app:`/`app.bundle:` contexts or tags to limit heavy grammars to the applications where you need them. For instance, enable the rich symbol/function-key grammar only in terminals/IDEs, keep browser/email contexts lighter.

Where to change:

- Split parts of `core/keys/keys.talon` into `core/applications/*.talon` or create per-app `.talon` with `tag()` enablement.

---

## 9) Consider a short anti-merger pause in letter names

If the engine sometimes merges adjacent letter names, choose spoken forms that naturally include a crisp stop or varied vowel shape, or add a very short glottal stop (habit) between letters. This is a speaking technique rather than a code change, but it often lifts accuracy immediately for rapid sequences.

---

## 10) Logging and iterative tuning

- Use `help alphabet` (see `README.md`) to practice and verify new forms.
- When a letter is misrecognized, note the “heard” text from history (`core/text/phrase_history.py`). Add 1–2 alternates for that letter that are phonetically far from the mistake.
- Make one change at a time, test for a day, keep what helps, revert what doesn’t.

---

## 11) Summary of suggested edits (when you’re ready)

No changes have been applied. When you want to proceed, here are the concrete edits I’d start with:

- Adjust `speech.timeout` in `settings.talon` to 0.4–0.5 and iterate.
- In `core/keys/letter.talon-list`:
  - Remove near-duplicates (pick either `ish` or `esh` for `e`).
  - Replace English words: `queue` (q) → non-word alternative; `you` (u) → non-word alternative; `ex` (x) → non-word alternative; `wise` (y) → non-word alternative.
  - Add 1–2 alternates only for chronically missed letters.
- If needed, add a `spell …` prefix context to constrain one-utterance sequences to `<user.letters>`.
- Rename or relocate any vocabulary entries (e.g., `esnore`) that collide with command phrases, especially if you plan to use mixed mode.

If you’d like, I can implement these incrementally with toggles so you can A/B test changes safely.



