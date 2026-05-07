### Planning: Java keyword spoken forms for Chrome coding contexts

#### Context

The user dictates Java code exclusively in Chrome, on coding-interview websites (e.g. neetcode.io, company-provided platforms). There is no IDE Talon integration active — no `code.language: java` tag, no language mode detection. Commands must work in a plain browser text editor (usually CodeMirror or Monaco).

Current workaround: short Java keywords that the recognizer mishears are spelled out using the custom alphabet. Known case:

| Keyword | Problem | Current workaround |
|---------|---------|-------------------|
| `int`   | heard as "into" | `ice near trap space` |

---

#### How upstream handles it

Upstream ([talonhub-community/lang/java/](C:\Users\hamou\Documents\talonhub-community\lang\java\)) defines a `user.code_keyword` list in [code_keyword.talon-list](C:\Users\hamou\Documents\talonhub-community\lang\java\code_keyword.talon-list) tagged `code.language: java`. When that tag is active, spoken "int" maps to `"int "` unambiguously — the grammar is narrowed to Java keywords, so the recognizer has no reason to prefer "into".

It also defines `user.code_type` (primitives + boxed types) and `user.code_common_method` for things like `println`, `toString`, etc.

The tag becomes active via Talon's IDE plugins (VS Code extension, IntelliJ plugin) which detect the open file's language and broadcast a tag. **None of that applies to Chrome.**

---

#### The problem to solve

Without a narrowing tag, any Java keyword that is also a plausible English word competes against the speech engine's language model:

| Keyword     | Likely mishearing |
|-------------|-------------------|
| `int`       | "into"            |
| `char`      | "char" (possibly ok, unusual word) |
| `byte`      | "bite" / "bight"  |
| `void`      | probably ok       |
| `boolean`   | probably ok (long enough) |
| `float`     | probably ok       |
| `long`      | probably ok       |
| `short`     | probably ok       |
| `var`       | possibly "far", "bar" |
| `instanceof`| must be spelled via `smash instance of over` anyway |

---

#### Options

**Option A — Spell ambiguous keywords with the alphabet**

Already working for `int` → `ice near trap space`. Extend to any other keyword that misfires in practice.

- Pros: no new files, no new Talon infrastructure.
- Cons: verbose; mentally translating `int` to `ice near trap` has a learning curve.

**Option B — Define a narrow `.talon` file scoped to Chrome with explicit keyword mappings**

Add a file like `apps/chrome/java_keywords.talon` with a header `app: chrome` (and optionally `tag: user.java_mode` if a toggle is desired). Inside, map short spoken aliases to `insert("int ")` etc.

Example:
```talon
app: chrome
-
keen: insert("int ")
```

Or just reuse the exact spoken word but pipe it through `insert()` instead of the dictation engine, so Talon wins over the speech model:

```talon
app: chrome
-
int: insert("int ")
char: insert("char ")
var: insert("var ")
byte: insert("byte ")
```

- Pros: clean, no spelling, mirrors upstream's intent.
- Cons: adds a Chrome-scoped file; `int` as a command form may still collide with dictation if mixed mode is ever used; `app: chrome` is broad (fires in ALL Chrome tabs, not just coding sites).

**Option C — Tag-gated file + manual toggle**

Add a `user.java_mode` tag that can be toggled with a voice command (e.g. "java mode on" / "java mode off"), then scope the keyword file to that tag. Works in any app including Chrome.

- Pros: precise; doesn't pollute the global grammar; mirrors upstream's structure.
- Cons: requires remembering to toggle; adds mode machinery (the fork deliberately keeps modes minimal).

**Option D — Borrow upstream's `code.language` tag but activate it manually**

Talon allows defining a tag in a `.talon` file unconditionally. We could activate `code.language: java` via a voice toggle, then import upstream's `code_keyword.talon-list` as-is.

- Pros: reuses upstream's complete keyword list (all 60+ keywords already mapped); minimal maintenance.
- Cons: `code.language: java` is upstream's tag convention — it implies IDE integration semantics and may interact unexpectedly if any other upstream file also checks that tag. Requires auditing which upstream files would activate.

---

#### Recommendation (deferred — for future session)

Option B (Chrome-scoped explicit commands) is the lowest-friction path for a coding-interview use case:
- No toggle to remember.
- Only fires in Chrome, so it doesn't affect other apps.
- Small file, easy to maintain.
- Can be narrowed further with `url: /neetcode\.io/` etc. if Chrome-wide keywords cause problems.

Option C (tag toggle) is better if the keywords ever interfere with normal browsing in Chrome.

Before committing, audit which other keywords (beyond `int`) actually misfire in practice during a real coding session — the fix scope may be small.

---

#### Open questions

- Does `char` misfire? (`byte`? `var`?)
- Is `app: chrome` the right header, or does this fork use a different app name for Chrome? Check `apps/chrome/` or run `talon.app_name()` in Chrome to confirm.
- Should the file include a trailing space after each keyword (like upstream does: `"int "`) or leave spacing to the next spoken form? Trailing space is friendlier for flowing dictation.
