# Enables only one of the two IDE tags at a time (“use intellij”, “use visual studio”)
from talon import Module, actions, app

mod = Module()

INTELLIJ = "user.intellij"
VSCODE   = "user.vscode"
ALL_TAGS = (INTELLIJ, VSCODE)

def _enable_only(tag: str):
    for t in ALL_TAGS:
        if t == tag:
            actions.user.tag_enable(t)
        else:
            actions.user.tag_disable(t)

@mod.action_class
class Actions:
    def switch_to_intellij():
        """Voice‑toggle IntelliJ command set"""
        _enable_only(INTELLIJ)
        app.notify("Switched to IntelliJ")

    def switch_to_vscode():
        """Voice‑toggle VS Code command set"""
        _enable_only(VSCODE)
        app.notify("Switched to VS Code")
