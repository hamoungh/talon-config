app: /IntelliJ IDEA/
-

# ---- navigation & tool windows ----
zi fixi:                   key(alt-enter)
zi format:                 key(cmd-alt-l)
zi terminal:               key(alt-f12)
zi callgraph:              key(cmd-alt-h)
zi type hierarchy:         key(cmd-h)
zi resize:                 key(ctrl:down)
zi file:                   key(shift-cmd-n)
zi project:                key(cmd-1)
zi structure:              key(cmd-7)
zi source control:         key(cmd-9)

# ---- search / refactor ----
zi search everywhere:      key(shift-shift)
zi find everywhere:        key(shift-cmd-f)
zi find | zi search:       key(cmd-f)
zi replace:                key(cmd-r)
zi replace everywhere:     key(shift-cmd-r)
zi fold all:               key(shift-cmd-minus)
zi go to:                  key(cmd-alt-b)
zi usage:                  key(alt-shift-7)
zi surround with:          key(cmd-alt-t)

# ---- shell helpers ----
zi go in:
    key(cmd-c)
    insert("cd ")
    key(cmd-v)
    insert(";ls")
    key(enter)

zi go up:
    insert("cd ..;ls")
    key(enter)

zi list:
    insert("ls")
    key(enter)

zi find process:
    insert("ps aux|grep ")

# ---- misc ----
zi comment:                key(cmd-/)
zi run:
    key(home)
    key(shift-end)
    key(cmd-c)
    key(alt-f12)
    key(cmd-v)
    key(enter)

zi command:                key(shift-cmd-p)
zi imports:                key(cmd-alt-o)
zi exe:                    key(shift-alt-e)
always on top:             key(cmd-t)

# zi run old:
#     key(home) key(shift-end)
#     key(cmd-c)
#     key(alt-f12)
#     key(cmd-v)
#     key(enter)

# zi run:
# zi run: 