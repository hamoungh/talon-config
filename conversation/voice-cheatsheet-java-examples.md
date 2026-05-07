### Talon voice examples — dictating Java

Worked examples of the customized grammar in this fork applied to common Java code.
Companion to [voice-cheatsheet.md](voice-cheatsheet.md) (alphabet, symbols, formatters)
and [voice-cheatsheet-windows.md](voice-cheatsheet-windows.md) (editing/navigation).

#### Quick rules to remember

- **Code formatters are greedy.** `hammer`, `nace`, `zake`, `zabe`, `dub string`, `string`, `hake`, etc. consume words until end-of-breath or the phrase-ender **`over`**. To chain anything after a code formatter in the same utterance, end it with `over`.
- **Word formatters are non-greedy and chainable**, one word each:
  - `word foo` → `foo`
  - `trot foo` → `foo ` (trailing space)
  - `proud foo` → `Foo`
  - `leap foo` → `Foo ` (capitalize + trailing space)
- **Single letters** (`arch`, `bat`, `cage`, … `each`, … `ice`, …) type the literal letter directly — useful for loop variables.
- **`space`** types a literal space; **`slap`** is Enter.
- Symbols you'll lean on most in Java (all command-mode forms): `L paren` `R paren` `L brace` `R brace` `L bracket` `R bracket` `dot` `comma` `semi` `colon` `equals` `dash` `greater than` `less than` `bang` `at sign` `double quote` `plus` `minus` `slash`.

---

#### Class & method skeletons

| Voice                                                                                              | Output                                  |
|----------------------------------------------------------------------------------------------------|-----------------------------------------|
| `trot public trot class hammer hello world over space L brace`                                     | `public class HelloWorld {`             |
| `trot public trot static trot void nace main over L paren leap string L bracket R bracket word args R paren space L brace` | `public static void main(String[] args) {` |
| `trot public ice near trap space nace get count over L paren R paren space L brace`                | `public int getCount() {`               |
| `trot private trot void nace set name over L paren leap string word name R paren space L brace`   | `private void setName(String name) {`   |
| `at sign proud override`                                                                           | `@Override`                             |
| `R brace`                                                                                          | `}`                                     |

#### Variable declarations & constants

| Voice                                                                                              | Output                                       |
|----------------------------------------------------------------------------------------------------|----------------------------------------------|
| `ice near trap space word count space equals space zero semi`                                       | `int count = 0;`                             |
| `trot final leap string word greeting space equals space double quote proud hello double quote semi` | `final String greeting = "Hello";`     |
| `trot private trot static trot final ice near trap space zabe max size over space equals space 100 semi` | `private static final int MAX_SIZE = 100;`   |
| `leap string L bracket R bracket word names space equals space L brace double quote proud bob double quote comma space double quote proud sue double quote R brace semi` | `String[] names = {"Bob", "Sue"};` |
| `word var word total space equals space word a space plus space word b semi`                  | `var total = a + b;`                         |

> `trot foo` for any single lowercase keyword (`public`, `final`, `static`, `return`, `import`, `if`, `for`, `while`, `try`, `catch`, `new`, `this`, `void`, `else`, `case`, `break`) is the workhorse pattern — outputs the word with a trailing space, ready for the next token. **Exception: `int`** — the recognizer hears it as "into". Spell it instead: `ice near trap space`.

#### Method calls & dot chains

| Voice                                                                                              | Output                                  |
|----------------------------------------------------------------------------------------------------|-----------------------------------------|
| `proud system dot word out dot word println L paren double quote proud hello double quote R paren semi` | `System.out.println("Hello");` |
| `word user dot nace get name over L paren R paren`                                                 | `user.getName()`                        |
| `word list dot word size L paren R paren`                                                          | `list.size()`                           |
| `word str dot nace to lower case over L paren R paren dot nace trim over L paren R paren`          | `str.toLowerCase().trim()`              |
| `proud math dot word max L paren word a comma space word b R paren`                                | `Math.max(a, b)`                        |

> Between dotted segments use `word foo` (no trailing space) so the dots stay tight.

#### Strings, concatenation, escapes

| Voice                                                                                              | Output                                  |
|----------------------------------------------------------------------------------------------------|-----------------------------------------|
| `dub string hello world over`                                                                      | `"hello world"`                         |
| `double quote proud hello comma space proud world bang double quote`                               | `"Hello, World!"`                       |
| `leap string word msg space equals space double quote proud hello comma space double quote space plus space word name semi` | `String msg = "Hello, " + name;` |
| `double quote proud line backslash word n proud next double quote`                                 | `"Line\nNext"`                          |

> The `dub string` greedy formatter is fastest for ALL-LOWERCASE strings. For anything mixed case or with punctuation inside, fall through to the explicit `double quote … double quote` form.

#### Control flow

| Voice                                                                                              | Output                                  |
|----------------------------------------------------------------------------------------------------|-----------------------------------------|
| `trot if L paren word count space greater than space 0 R paren space L brace`                     | `if (count > 0) {`                      |
| `R brace space trot else space L brace`                                                            | `} else {`                              |
| `trot for L paren ice near trap space ice space equals space zero semi space ice space less than space 10 semi space ice plus plus R paren space L brace` | `for (int i = 0; i < 10; i++) {` |
| `trot for L paren leap string word name colon space word names R paren space L brace`              | `for (String name : names) {`           |
| `trot while L paren word ready R paren space L brace`                                              | `while (ready) {`                       |
| `trot switch L paren word status R paren space L brace`                                            | `switch (status) {`                     |
| `trot case zabe active over colon`                                                                 | `case ACTIVE:`                          |
| `trot break semi`                                                                             | `break;`                                |
| `trot return word true semi`                                                                  | `return true;`                          |

#### Try / catch / throw

| Voice                                                                                              | Output                                  |
|----------------------------------------------------------------------------------------------------|-----------------------------------------|
| `trot try space L brace`                                                                           | `try {`                                 |
| `R brace space trot catch L paren proud exception space each R paren space L brace`                | `} catch (Exception e) {`               |
| `trot throw trot new hammer illegal argument exception over L paren double quote proud bad input double quote R paren semi` | `throw new IllegalArgumentException("Bad input");` |
| `trot throws hammer io exception over comma space hammer sql exception over`                       | `throws IOException, SQLException`      |

#### Collections, generics, instanceof

| Voice                                                                                              | Output                                       |
|----------------------------------------------------------------------------------------------------|----------------------------------------------|
| `proud list less than proud string greater than space word names space equals space trot new hammer array list over less than greater than L paren R paren semi` | `List<String> names = new ArrayList<>();` |
| `proud map less than proud string comma space proud integer greater than space word counts space equals space trot new hammer hash map over less than greater than L paren R paren semi` | `Map<String, Integer> counts = new HashMap<>();` |
| `word names dot word add L paren double quote proud alice double quote R paren semi`         | `names.add("Alice");`                        |
| `trot if L paren word obj space smash instance of over space proud string space each R paren space L brace` | `if (obj instanceof String e) {`     |

#### Lambdas & streams

| Voice                                                                                              | Output                                  |
|----------------------------------------------------------------------------------------------------|-----------------------------------------|
| `word names dot nace for each over L paren word name space dash greater than space proud system dot word out dot word println L paren word name R paren R paren semi` | `names.forEach(name -> System.out.println(name));` |
| `word numbers dot word stream L paren R paren dot word filter L paren word n space dash greater than space word n space greater than space 0 R paren dot nace to list over L paren R paren` | `numbers.stream().filter(n -> n > 0).toList()` |
| `word users dot word stream L paren R paren dot word map L paren proud user space colon colon space nace get name over R paren` | `users.stream().map(User :: getName)` |

> Method reference `::` has no built-in spoken form here; use `colon colon`. (Or define `packed` more loosely — currently `packed` is a code formatter that joins words with `::`, not a literal symbol.)

#### Annotations & imports

| Voice                                                                                              | Output                                  |
|----------------------------------------------------------------------------------------------------|-----------------------------------------|
| `at sign proud override`                                                                           | `@Override`                             |
| `at sign proud deprecated`                                                                         | `@Deprecated`                           |
| `at sign nace suppress warnings over L paren dub string unchecked over R paren`                    | `@SuppressWarnings("unchecked")`        |
| `trot package word com dot word example dot word app semi`                                    | `package com.example.app;`              |
| `trot import word java dot word util dot hammer array list over semi`                         | `import java.util.ArrayList;`           |
| `trot import trot static word java dot word lang dot proud math dot word max semi`            | `import static java.lang.Math.max;`     |

#### Comments

| Voice                                                                                              | Output                                  |
|----------------------------------------------------------------------------------------------------|-----------------------------------------|
| `slash slash space sentence handle empty input`                                                    | `// Handle empty input`                 |
| `slash slash space zabe todo over colon space say validate user`                                   | `// TODO: validate user`                |
| `slash star star slap`                                                                             | `/**` (then newline — start of Javadoc) |
| `space star space at sign word param space word name space sentence the user name`                 | ` * @param name The user name`          |

#### When you need `over`

Code formatters match the rule `<user.format_code>+$` in [core/text/text.talon](core/text/text.talon) — they consume words until end-of-utterance or the phrase-ender **`over`** (the only entry in [core/text/phrase_ender.talon-list](core/text/phrase_ender.talon-list)). Anything that follows a code formatter in the same breath is sucked in as text unless `over` closes it first.

Side-by-side — same intent, with and without the terminator:

| Spoken (broken)                                            | Spoken (correct)                                                | Intended output                  | What the broken form actually produces                |
|------------------------------------------------------------|-----------------------------------------------------------------|----------------------------------|--------------------------------------------------------|
| `zake user id semi`                                        | `zake user id over semi`                                        | `user_id;`                       | `user_id_semi` — `semi` eaten as a word                |
| `hammer array list L paren R paren`                        | `hammer array list over L paren R paren`                        | `ArrayList()`                    | `ArrayListLParenRParen` — symbol words all consumed    |
| `at sign nace suppress warnings L paren dub string unchecked over R paren` | `at sign nace suppress warnings over L paren dub string unchecked over R paren` | `@SuppressWarnings("unchecked")` | `@suppressWarningsLParenDubStringUncheckedOverRParen` |
| `hammer custom type greater than`                          | `hammer custom type over greater than`                          | `CustomType>`                    | `CustomTypeGreaterThan`                                |
| `nace get email dot word value`                            | `nace get email over dot word value`                            | `getEmail.value`                 | `getEmailDotWordValue`                                 |
| `trot return nace get name semi`                           | `trot return nace get name over semi`                           | `return getName;`                | `return getNameSemi`                                   |

> Word formatters (`word`, `trot`, `proud`, `leap`) only consume **one** word, so they never need `over`. Only the greedy code formatters (`hammer`, `nace`, `zake`, `zabe`, `hake`, `dotted`, `dub string`, `string`, `smash`, `slasher`, `conga`, `packed`, `padded`, `all cap`, `all down`, `dunder`) require it.

When you can drop `over`:

- The code formatter is the **last** thing in the utterance — `$` (end of utterance) terminates it for you. `trot return zake user id` → `return user_id` ✓ (then pause and start the next utterance for the `;`).
- You're inside a multi-formatter chain like `<user.format_code>+`. In practice this is fragile and Talon's parser may bind words to whichever formatter wins — always safer to insert `over` between formatters.

Concrete examples of `over` doing real work in this fork:

| Voice                                                                              | Output                          | Why `over` is needed                          |
|------------------------------------------------------------------------------------|---------------------------------|-----------------------------------------------|
| `nace get user name over L paren R paren`                                          | `getUserName()`                 | block `L paren` from being absorbed           |
| `hammer http request builder over dot word build L paren R paren`                  | `HttpRequestBuilder.build()`    | block `dot` and the chained method            |
| `dub string error colon space proud not found over space plus space word details`  | `"error: Not Found" + details`  | close the string formatter before `space plus space` |
| `trot if L paren word obj space smash instance of over space proud string R paren` | `if (obj instanceof String)`    | join `instance` + `of` then resume normal commands |
| `zake first name over space equals space double quote proud john double quote semi`| `first_name = "John";`          | snake_case the identifier, then continue the assignment |
| `at sign nace request mapping over L paren dub string slash users over R paren`    | `@RequestMapping("/users")`     | terminate the annotation name AND the URL string |

Notice the last row uses `over` **twice** in one utterance — once after `nace request mapping` (to close the privateCase identifier) and once after `dub string slash users` (to close the string literal). Each greedy formatter needs its own terminator.

#### Putting it together: a small worked example

Goal:

```java
@Override
public String toString() {
    return "user_id=" + userId;
}
```

Utterance by utterance (pause between each):

1. `at sign proud override slap`
2. `trot public leap string nace to string over L paren R paren space L brace slap`
3. `trot return double quote zake user id over equals double quote space plus space nace user id over semi slap`
4. `R brace`

The third utterance is what actually exercises the formatters: `zake user id over` joins two words into `user_id` (snake_case), and `nace user id over` joins the same two words into `userId` (privateCase). Both formatters are greedy, so each is closed with `over` before the next non-word token (`equals`, `semi`).

---

#### Tips for accuracy on long Java lines

- **Break at clause boundaries.** One utterance per line of code is usually fastest. Talon's recognizer struggles with long chains; pausing after `slap` (newline) lets it reset.
- **Anchor with `over` aggressively.** Whenever a code formatter is followed by anything that isn't more words, terminate with `over`. The cost is one syllable; the benefit is no surprise concatenation.
- **Use `proud`/`leap` over `hammer` for one-word identifiers.** `hammer foo over` and `proud foo` both produce `Foo`, but `proud foo` is non-greedy and one syllable shorter.
- **Spell tricky tokens.** For unusual identifiers (`xy`, `iy`, abbreviations) the letter alphabet (`plex yank`, `ice yank`) is more reliable than dictation.
- **Prefer `edit.*` for navigation** between utterances — `line end`, `line start`, `slap`, `tab` — rather than embedding cursor moves in the same breath as a code formatter.
