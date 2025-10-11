from talon import Module

mod = Module()


apps = mod.apps

# apple specific apps
apps.datagrip = """
os: mac
and app.name: DataGrip
"""

apps.finder = """
os: mac
and app.bundle: com.apple.finder
"""

apps.rstudio = """
os: mac
and app.name: RStudio
"""

apps.apple_terminal = """
os: mac
and app.bundle: com.apple.Terminal
"""

# linux specific apps
apps.keepass = """
os: linux
and app.name: KeePassX2
os: linux
and app.name: KeePassXC
os: linux
and app.name: KeepassX2
os: linux
and app.name: keepassx2
os: linux
and app.name: keepassxc
os: linux
and app.name: Keepassxc"""

apps.signal = """
os: linux
and app.name: Signal

os: linux
and app.name: signal
"""

apps.termite = """
os: linux
and app.name: /termite/
"""

apps.windows_command_processor = r"""
os: windows
and app.name: Windows Command Processor
os: windows
and app.exe: /^cmd\.exe$/i
"""

apps.windows_terminal = r"""
os: windows
and app.exe: /^windowsterminal\.exe$/i
"""

mod.apps.windows_power_shell = r"""
os: windows
and app.exe: /^powershell\.exe$/i
"""

apps.vim = """
win.title:/VIM/
"""


# DataGrip (JetBrains)
apps.datagrip = r"""
os: mac
and app.bundle: com.jetbrains.datagrip
os: mac
and app.name: DataGrip
"""

# IntelliJ IDEA (Ultimate + Community)
apps.intellij = r"""
# macOS: prefer bundle prefix for reliability, with name fallbacks
os: mac
and app.bundle: /^com\.jetbrains\./
os: mac
and app.name: /^IntelliJ/
os: mac
and app.name: /^JetBrains/
os: mac
and app.name: /^Gateway/

"""

# RStudio
apps.rstudio = r"""
os: mac
and app.bundle: org.rstudio.RStudio
os: mac
and app.name: RStudio
"""

# VS Code (fixed from your original)
apps.vscode = r"""
os: mac
and app.bundle: com.microsoft.VSCode
os: mac
and app.bundle: com.microsoft.VSCodeInsiders
# Optional name fallbacks
os: mac
and app.name: Code
os: mac
and app.name: Visual Studio Code
"""

# Cursor (keep name; bundle id can vary between builds)
apps.cursor = r"""
os: mac
and app.name: Cursor
"""