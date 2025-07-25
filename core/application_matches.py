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

apps.cursor = """
os: mac
and app.name: Cursor
"""

apps.vscode = """
os: mac
and app.name: Visual Studio Code
"""

apps.intellij = """
os: mac
and app.name: IntelliJ IDEA
"""
