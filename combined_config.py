from dragonfly import *  # noqa: F401,F403
import logging
import types
from time import sleep

# ---------------------------------------------------------------------------
# Shared namespace (used by several rules to share RuleRefs)
# ---------------------------------------------------------------------------
shared = types.SimpleNamespace()

# ---------------------------------------------------------------------------
# Helper formatting functions (originating from format.py)
# ---------------------------------------------------------------------------
def _format_score(dictation):
    text = str(dictation)
    words = [word.lower() for word in text.split(" ")]
    Text("_".join(words)).execute()


def _format_title(dictation):
    text = str(dictation)
    words = [word.capitalize() for word in text.split(" ")]
    Text(" ".join(words)).execute()


def _format_jake(dictation):
    text = str(dictation)
    words = [word.lower() for word in text.split(" ")]
    Text(" ".join(words)).execute()


def _format_studley(dictation):
    text = str(dictation)
    words = [word.capitalize() for word in text.split(" ")]
    Text("".join(words)).execute()


def _format_one_word(dictation):
    text = str(dictation)
    words = [word.lower() for word in text.split(" ")]
    Text("".join(words)).execute()


def _format_upper_one_word(dictation):
    text = str(dictation)
    words = [word.upper() for word in text.split(" ")]
    Text("".join(words)).execute()


def _format_dotword(dictation):
    text = str(dictation)
    words = [word.lower() for word in text.split(" ")]
    Text(".".join(words)).execute()


def _format_upper_score(dictation):
    text = str(dictation)
    words = [word.upper() for word in text.split(" ")]
    Text("_".join(words)).execute()


def _format_jive(dictation):
    text = str(dictation)
    words = [word.lower() for word in text.split(" ")]
    Text("-".join(words)).execute()


def _format_java_method(dictation):
    text = str(dictation)
    words = text.split(" ")
    Text(words[0].lower() + "".join(w.capitalize() for w in words[1:])).execute()


# ---------------------------------------------------------------------------
# FormatRule (originating from format.py)
# ---------------------------------------------------------------------------
class FormatRule(MappingRule):
    mapping = {
        "zake <dictation>": Function(_format_score),
        "say <dictation>": Function(_format_jake),
        "hake <dictation>": Function(_format_jive),
        "dake <dictation>": Function(_format_dotword),
        "jait <dictation>": Function(_format_title),
        "nate <dictation>": Function(_format_studley),
        "nake  <dictation>": Function(_format_one_word),
        "nabe <dictation>": Function(_format_upper_one_word),
        "zabe <dictation>": Function(_format_upper_score),
        "nace <dictation>": Function(_format_java_method),
    }
    extras = [Dictation("dictation")]


# ---------------------------------------------------------------------------
# LetterRule (originating from letterRule.py)
# ---------------------------------------------------------------------------
class LetterRule(MappingRule):
    exported = True
    mapping = {
        'ach': Key('a', static=True),
        'bik': Key('b', static=True),
        'kaj': Key('c', static=True),
        'daf': Key('d', static=True),
        'ish': Key('e', static=True),
        'fick': Key('f', static=True),
        'goeff': Key('g', static=True),
        'hash': Key('h', static=True),
        'jack': Key('j', static=True),
        'kif': Key('k', static=True),
        'laam': Key('l', static=True),
        'meem': Key('m', static=True),
        'noon': Key('n', static=True),
        'paf': Key('p', static=True),
        'queue': Key('q', static=True),  # queue
        'rij': Key('r', static=True),
        'saad': Key('s', static=True),
        'tenj': Key('t', static=True),
        'vazz': Key('v', static=True),
        'wek': Key('w', static=True),  # doubleu
        'ex': Key('x', static=True),  # ex
        'wise': Key('y', static=True),  # waay
        'zed': Key('z', static=True),
        'esh': Key('e', static=True),
        'you': Key('u', static=True),  # you
        'osh': Key('o', static=True),
        'ice': Key('i', static=True),

        'zero': Key('0'),
        'one': Key('1'),
        'two': Key('2'),
        'three': Key('3'),
        'four': Key('4'),
        'five': Key('5'),
        'six': Key('6'),
        'seven': Key('7'),
        'eight': Key('8'),
        'nine': Key('9'),

        'jet': Key('space'),
        'soot': Key("win:up, alt:up, escape"),

        'tab': Key('tab'),

        'amphi': Key('ampersand'),
        'quote': Key('apostrophe'),
        '[single] quote': Key('squote'),
        'saar': Key('asterisk'),
        'atsi': Key('at'),
        'bash': Key('backslash'),
        'tick': Key('backtick'),
        'bar': Key('bar'),
        'cart': Key('caret'),
        'colx': Key('colon'),
        'kooch': Key('comma'),
        'dollar': Key('dollar'),
        '(dot|period)': Key('dot'),
        'duote': Key('dquote'),
        'moss': Key('equal'),
        'bang': Key('exclamation'),
        'sharp': Key('hash'),
        'hyph': Key('hyphen'),
        'pers': Key('percent'),
        'pulse': Key('plus'),
        'kess': Key('question'),
        'semi': Text(";"),
        'sash': Key('slash'),

        'tilde': Key('tilde'),
        'zoor': Key('underscore'),
        'langle': Key('langle'),
        'lace': Key('lbrace'),
        'lack': Key('lbracket'),
        'laip': Key('lparen'),
        'rangle': Key('rangle'),
        'race': Key('rbrace'),
        'rack': Key('rbracket'),
        'raip': Key('rparen'),
    }


# ---------------------------------------------------------------------------
# KeystrokeRule (originating from keystroke.py)
# ---------------------------------------------------------------------------
class KeystrokeRule(MappingRule):
    release = Key("shift:up, ctrl:up")

    mapping = {
        "[<n>] up": Key("up/2:%(n)d"),
        "[<n>] down": Key("down/2:%(n)d"),
        "[<n>] left": Key("left/2:%(n)d"),
        "[<n>] right": Key("right/2:%(n)d"),
        "[<n>] pop": Key("pgup/2:%(n)d"),
        "[<n>] pen": Key("pgdown/2:%(n)d"),
        "<n> up (page | pages)": Key("pgup/2:%(n)d"),
        "<n> down (page | pages)": Key("pgdown/2:%(n)d"),
        "<n> left (word | words)": Key("c-left/2:%(n)d"),
        "<n> right (word | words)": Key("c-right/2:%(n)d"),
        "home": Key("home"),
        "end": Key("end"),
        "doc home": Key("c-home"),
        "doc end": Key("c-end"),
        "follow": Key("ctrl:down") + Mouse("left") + Key("ctrl:up"),
        "[<n>] slap": release + Key("enter/2:%(n)d"),
        "[<n>] tab": Key("tab/2:%(n)d"),
        "[<n>] dij": release + Key("del/2:%(n)d"),
        "ditch [<n> | this] (line|lines)": release + Key("home, s-down/2:%(n)d, del"),
        "[<n>] boot": release + Key("backspace/2:%(n)d"),
        "pop up": release + Key("apps"),
        "pinj": release + Key("c-v"),
        "duplicate <n>": release + Key("c-c, c-v:%(n)d"),
        "copy": release + Key("c-c"),
        "thatsy": release + Key("c-c"),
        "cut": release + Key("c-x"),
        "select all": release + Key("c-a"),
        "[hold] shi": Key("shift:down"),
        "shiffup": Key("shift:up"),
        "[hold] zoo": Key("ctrl:down"),
        "contup": Key("ctrl:up"),
        "[hold] az": Key("alt"),
        "altup": Key("alt:up"),
        "release [all]": release,
        "tux": Key("c-a"),
        "amplify": Key("c-plus"),
        "mimic <text>": release + Mimic(extra="text"),
        "efyek": Key("f1"),
        "efdouce": Key("f2"),
        "efse": Key("f3"),
        "efchar": Key("f4"),
        "efpanj": Key("f5"),
        "efshish": Key("f6"),
        "efhaf": Key("f7"),
        "efhash": Key("f8"),
        "efnoh": Key("f9"),
        "efdah": Key("f10"),
        "efyazdah": Key("f11"),
        "efdavazdah": Key("f12"),
        "efsizdah": Key("f13"),
        "efcharda": Key("f14"),
        "efpoonza": Key("f15"),
        "inteli jey": Text("intellij"),
    }
    extras = [
        IntegerRef("n", 1, 100),
        Dictation("text"),
        Dictation("text2"),
    ]
    defaults = {"n": 1}


# ---------------------------------------------------------------------------
# Initialize shared RuleRefs so that other rules (e.g. RepeatRule) can use them
# ---------------------------------------------------------------------------
shared.letter = RuleRef(rule=LetterRule(), name='letter')
shared.keystroke = RuleRef(rule=KeystrokeRule(), name='keystroke')
shared.letter_sequence = Repetition(shared.letter, min=1, max=32, name='letter_sequence')


# ---------------------------------------------------------------------------
# RepeatRule (originating from repeatt.py)
# ---------------------------------------------------------------------------
class RepeatRule(CompoundRule):
    # Build list of alternatives on class definition so it's cached once
    _alternatives = [
        shared.keystroke,
        RuleRef(rule=FormatRule()),
        shared.letter,
    ]

    single_action = Alternative(_alternatives)
    sequence = Repetition(single_action, min=1, max=16, name="sequence")

    spec = "<sequence> <n> times]"
    extras = [
        sequence,
        IntegerRef("n", 1, 100),
    ]
    defaults = {"n": 1}

    def _process_recognition(self, node, extras):
        release = Key("shift:up, ctrl:up")
        sequence = extras["sequence"]
        count = extras["n"]
        for _ in range(count):
            for action in sequence:
                action.execute()
            sleep(0.05)
        release.execute()


# ---------------------------------------------------------------------------
# VS Code and IntelliJ specific rules (originating from _vscode.py and _intellij.py)
# ---------------------------------------------------------------------------
class VSCodeRule(MappingRule):
    mapping = {
        "always on top": Key("w-t"),
        "pilot": Key("a-left"),
        "zi callgraph": Text("Not directly available in VS Code"),
        "zi command": Key("c-s-p"),
        "zi comment": Key("c-slash"),
        "zi exe": Key("c-f5"),
        "zi file": Key("c-p"),
        "zi find": Key("c-f"),
        "zi find everywhere": Key("c-s-f"),
        "zi find process": Text("Get-Process | Where-Object {$_.Name -like '*'} | Format-Table Name, Id, CPU"),
        "zi fixi": Key("c-dot"),
        "zi fold all": Key("c-k, c-0"),
        "zi format": Key("s-a-f"),
        "zi go in": Key("c-c/25") + Pause("20") + Text("cd ") + Key("c-v/25") + Text(" && ls") + Key("enter/2"),
        "zi go to": Key("c-g"),
        "zi go up": Text("cd .. && ls") + Key("enter/2"),
        "zi imports": Key("c-s-o"),
        "zi list": Text("ls") + Key("enter"),
        "zi project": Key("c-b"),
        "zi replace": Key("c-h"),
        "zi replace everywhere": Key("c-s-h"),
        "zi resize": Key("c-backslash"),
        "zi run": Key("end, s-home, c-c/25") + Pause("20") + Key("c-backtick/25") + Pause("20") + Key("c-v/25") + Pause("20") + Key("enter"),
        "zi source control": Key("c-s-g"),
        "zi structure": Key("c-s-o"),
        "zi surround with": Key("c-k, c-s"),
        "zi terminal": Key("c-backtick"),
        "zi type hierarchy": Key("c-t"),
        "zi usage": Key("s-f12"),
    }


vscode_grammar = Grammar("vscode")
vscode_grammar.add_rule(VSCodeRule())
vscode_grammar.load()


class IntelliJRule(MappingRule):
    mapping = {
        "zi fixi": Key("a-enter/2"),
        "zi format": Key("ac-l/25"),
        "zi terminal": Key("a-f12"),
        "zi callgraph": Key("ac-h"),
        "zi type hierarchy": Key("c-h"),
        "zi resize": Key("ctrl:down "),
        "zi file": Key("cs-n"),
        "zi project": Key("a-1"),
        "zi structure": Key("a-7"),
        "zi source control": Key("a-9"),
        "zi search everywhere": Key("cs-f"),
        "zi find everywhere": Key("cs-f"),
        "zi find": Key("c-f"),
        "zi search": Key("c-f"),
        "zi replace": Key("c-r"),
        "zi replace everywhere": Key("cs-r"),
        "zi fold all": Key("cs-minus"),
        "zi go to": Key("ac-b/25:1/25"),
        "zi usage": Key("as-7"),
        "zi surround with": Key("ca-t"),
        "zi go in": Key("c-c/25") + Pause("40") + Text("cd ") + Pause("40") + Key("c-v/25") + Text(";ls") + Pause("40") + Key("enter/2"),
        "zi list": Text("ls") + Key("enter"),
        "zi go up": Text("cd ..") + Text(";ls") + Key("enter/2"),
        "zi find process": Text("ps aux|grep "),
        "zi comment": Key("c-slash"),
        "zi run": Key("home/25, s-end/25, c-c/25") + Pause("20") + Key("a-f12") + Pause("20") + Key("c-v/25") + Pause("20") + Key("enter"),
        "zi command": Key("cs-p"),
        "zi imports": Key("ca-o"),
        "zi exe": Key("as-e"),
        "always on top": Key("w-t"),
    }


intellij_grammar = Grammar("intellij")
intellij_grammar.add_rule(IntelliJRule())
intellij_grammar.load()
intellij_grammar.disable()  # Initially disabled (VS Code enabled by default)


# Expose module-like objects so that legacy references (_vscode.grammar etc.) still work
_vscode = types.SimpleNamespace(grammar=vscode_grammar)
_intellij = types.SimpleNamespace(grammar=intellij_grammar)


# ---------------------------------------------------------------------------
# Context switching rule (originating from _normal_rule.py -> IDEContext)
# ---------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("dragonfly.ide_context")


class IDEContext(MappingRule):
    def __init__(self):
        self.current_context = "vscode"  # Default context
        logger.info(f"IDEContext initialized. Current context: {self.current_context}")

        mapping = {
            "use intellij": Function(lambda: self.switch_context("intellij")),
            "use visual studio": Function(lambda: self.switch_context("vscode")),
        }

        super(IDEContext, self).__init__(mapping=mapping)

    def switch_context(self, context):
        logger.info(f"Attempting to switch context from {self.current_context} to {context}")

        if context == self.current_context:
            logger.info(f"Already in {context} context. No switch necessary.")
            return

        if context == "intellij":
            vscode_grammar.disable()
            intellij_grammar.enable()
            logger.info("Disabled VS Code grammar and enabled IntelliJ grammar")
        elif context == "vscode":
            intellij_grammar.disable()
            vscode_grammar.enable()
            logger.info("Disabled IntelliJ grammar and enabled VS Code grammar")
        else:
            logger.warning(f"Unknown context: {context}. No switch performed.")
            return

        self.current_context = context
        logger.info(f"Successfully switched to {context} context")
        print(f"Switched to {context} context")


# ---------------------------------------------------------------------------
# SnoreRule (originating from _snore.py) – put mic to sleep
# ---------------------------------------------------------------------------
try:
    import natlink  # natlink is only available inside Dragonfly / NatSpeak runtime
except ImportError:
    natlink = None


class SnoreRule(CompoundRule):
    spec = "esnore"  # Hard-coded string from original config

    def _process_recognition(self, node, extras):
        self._log.debug("sleepy mic")
        if natlink:
            natlink.setMicState("sleeping")


snore_grammar = Grammar("snore")
snore_grammar.add_rule(SnoreRule())
snore_grammar.load()


# ---------------------------------------------------------------------------
# Normal grammar combining everything
# ---------------------------------------------------------------------------
normal_grammar = Grammar("normal grammar")
normal_grammar.add_rule(IDEContext())
normal_grammar.add_rule(RepeatRule())
normal_grammar.load()
print("Dragonfly grammars loaded")


# ---------------------------------------------------------------------------
# Unload helper so that Dragonfly/NatLink can reload this file cleanly
# ---------------------------------------------------------------------------
def unload():
    global normal_grammar, vscode_grammar, intellij_grammar, snore_grammar
    for g in [normal_grammar, vscode_grammar, intellij_grammar, snore_grammar]:
        if g:
            g.unload()
    normal_grammar = None
    vscode_grammar = None
    intellij_grammar = None
    snore_grammar = None 