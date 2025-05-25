from talon import Module, actions

mod = Module()



def _words(text: str):
    return text.split()


@mod.action_class
class Actions:
    def format_score(text: str):
        """some_words"""
        actions.insert("_".join(w.lower() for w in _words(text)))

    def format_title(text: str):
        """Some Words"""
        actions.insert(" ".join(w.capitalize() for w in _words(text)))

    def format_jake(text: str):
        """some words"""
        actions.insert(" ".join(w.lower() for w in _words(text)))

    def format_studley(text: str):
        """SomeWords"""
        actions.insert("".join(w.capitalize() for w in _words(text)))

    def format_one_word(text: str):
        """somewords"""
        actions.insert("".join(w.lower() for w in _words(text)))

    def format_upper_one_word(text: str):
        """SOMEWORDS"""
        actions.insert("".join(w.upper() for w in _words(text)))

    def format_dotword(text: str):
        """some.other.words"""
        actions.insert(".".join(w.lower() for w in _words(text)))

    def format_upper_score(text: str):
        """SOME_OTHER_WORDS"""
        actions.insert("_".join(w.upper() for w in _words(text)))

    def format_jive(text: str):
        """some-other-words"""
        actions.insert("-".join(w.lower() for w in _words(text)))

    def format_java_method(text: str):
        """someOtherWords"""
        words = _words(text)
        if not words:
            return
        actions.insert(words[0].lower() + "".join(w.capitalize() for w in words[1:])) 