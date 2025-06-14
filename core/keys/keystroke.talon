# number capture (1-100)
<user.number_small> up:                    key(up:{user.number_small})
<user.number_small> down:                  key(down:{user.number_small})
<user.number_small> left:                  key(left:{user.number_small})
<user.number_small> right:                 key(right:{user.number_small})
<user.number_small> pop:                   key(pgup:{user.number_small})
<user.number_small> pen:                   key(pgdown:{user.number_small})
<user.number_small> up (page | pages):     key(pgup:{user.number_small})
<user.number_small> down (page | pages):   key(pgdown:{user.number_small})
<user.number_small> left (word \| words):   key(alt-left:{user.number_small})
<user.number_small> right (word \| words):  key(alt-right:{user.number_small})

home:        key(home)
end:         key(end)
doc home:    key(cmd-home)
doc end:     key(cmd-end)
follow:
    key(ctrl:down)
    mouse(0)
    key(ctrl:up)

slap:                               key(enter)
<user.number_small> slap:           key(enter:{user.number_small})
tab:                                key(tab)
<user.number_small> tab:            key(tab:{user.number_small})
dij:                                key(delete)
<user.number_small> dij:            key(delete:{user.number_small})
ditch line:
    key(home)
    key(shift-down)
    key(delete)

ditch <user.number_small> (line | lines):
    key(home)
    key(shift-down:{user.number_small})
    key(delete)

boot:                    key(backspace)
<user.number_small> boot:         key(backspace:{user.number_small})
pop up:      key(apps)

pinj: key(cmd-v)
copy: key(cmd-c)
cut it:      key(cmd-x)
duplicate <user.number_small>:
    key(cmd-c)
    key(cmd-v:{user.number_small})
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