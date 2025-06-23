# number capture (1-100)
<number_small> up:                    key("up:{number_small}")
<number_small> down:                  key("down:{number_small}")
<number_small> left:                  key("left:{number_small}")
<number_small> right:                 key("right:{number_small}")
<number_small> up (page | pages):     key("pgup:{number_small}")
<number_small> down (page | pages):   key("pgdown:{number_small}")
<number_small> left (word | words):   key("alt-left:{number_small}")
<number_small> right (word | words):  key("alt-right:{number_small}")

home:        key(home)
end:         key(end)

slap:                               key(enter)
<number_small> slap:           key("enter:{number_small}")
tab:                                key(tab)
<number_small> tab:            key("tab:{number_small}")
dij:                                key(delete)
<number_small> dij:            key("delete:{number_small}")


boot:                    key(bksp)
<number_small> boot:         key("bksp:{number_small}")


jet:              key(space)
<number_small> jet:     key("space:{number_small}")

pop up:      key(apps)

pinch: key(cmd-v)
copy: key(cmd-c)
cuty:      key(cmd-x)
duplicate <number_small>:
    key(cmd-c)
    key("cmd-v:{number_small}")
select all:  key(cmd-a)



inteli jey:  insert("intellij")
undo: key(cmd-z) 