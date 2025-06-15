# number capture (1-100)
<number_small> up:                    key(up:{number_small})
<number_small> down:                  key(down:{number_small})
<number_small> left:                  key(left:{number_small})
<number_small> right:                 key(right:{number_small})
<number_small> pop:                   key(pgup:{number_small})
<number_small> pen:                   key(pgdown:{number_small})
<number_small> up (page | pages):     key(pgup:{number_small})
<number_small> down (page | pages):   key(pgdown:{number_small})
<number_small> left (word | words):   key(alt-left:{number_small})
<number_small> right (word | words):  key(alt-right:{number_small})

home:        key(home)
end:         key(end)
doc home:    key(cmd-home)
doc end:     key(cmd-end)
follow:
    key(ctrl:down)
    mouse(0)
    key(ctrl:up)

slap:                               key(enter)
<number_small> slap:           key(enter:{number_small})
tab:                                key(tab)
<number_small> tab:            key(tab:{number_small})
dij:                                key(delete)
<number_small> dij:            key(delete:{number_small})
ditch line:
    key(home)
    key(shift-down)
    key(delete)

ditch <number_small> (line | lines):
    key(home)
    key(shift-down:{number_small})
    key(delete)

boot:                    key(backspace)
<number_small> boot:         key(backspace:{number_small})
pop up:      key(apps)

pinj: key(cmd-v)
copy: key(cmd-c)
cut it:      key(cmd-x)
duplicate <number_small>:
    key(cmd-c)
    key(cmd-v:{number_small})
select all:  key(cmd-a)

[hold] shi:  key(shift:down)
shiffup:     key(shift:up)
[hold] zoo:  key(ctrl:down)
contup:      key(ctrl:up)
[hold] az:   key(alt:down)
altup:       key(alt:up)
release all: key(shift:up ctrl:up alt:up)

tux:         key(cmd-a)
amplify:     key(cmd-+)


inteli jey:  insert("intellij") 