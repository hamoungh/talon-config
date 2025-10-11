app: vscode
-

always on top:             key(cmd-t)
pilot:                     key(alt-left)
zi callgraph:              insert("Not directly available in VS Code")
zi command:                key(shift-cmd-p)
zi comment:                key(cmd-/)
zi exe:                    key(cmd-f5)
zi file:                   key(cmd-p)
zi find:                   key(cmd-f)
zi find everywhere:        key(cmd-shift-f)
zi fixi:                   key(cmd-.)
zi fold all:
    key(cmd-k)
    key(cmd-0)
zi format:                 key(shift-alt-f)
zi go in:
    key(cmd-c)
    insert("cd ")
    key(cmd-v)
    insert(" && ls")
    key(enter)
zi go to:                  key(cmd-g)
zi go up:
    insert("cd .. && ls")
    key(enter)
zi imports:                key(cmd-shift-o)
zi list:
    insert("ls")
    key(enter)
zi project:                key(cmd-b)
zi replace:                key(cmd-h)
zi replace everywhere:     key(cmd-shift-h)
zi resize:                 key(cmd-backslash)
zi run:
    key(cmd-l)
    key(cmd-c)
    key(ctrl-`)
    sleep(150ms)
    key(cmd-v)
    key(enter)

zi chat:
    key(cmd-c)
    key(ctrl-`)
    sleep(150ms)
    key(cmd-v)
    key(enter)
zi source control:         key(cmd-shift-g)
zi structure:              key(cmd-shift-o)
zi surround with:
    key(cmd-k)
    key(cmd-s)
zi terminal:               key(ctrl-`)
zi type hierarchy:         key(cmd-t)
zi usage:                  key(shift-f12)
