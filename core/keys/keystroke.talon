# number capture (1-100)
<number_small> up:                    key("up:{number_small}")
<number_small> down:                  key("down:{number_small}")
<number_small> left:                  key("left:{number_small}")
<number_small> right:                 key("right:{number_small}")
<number_small> up (page | pages):     key("pgup:{number_small}")
<number_small> down (page | pages):   key("pgdown:{number_small}")
<number_small> left (word | words):   key("alt-left:{number_small}")
<number_small> right (word | words):  key("alt-right:{number_small}")

<number_small> slap:           key("enter:{number_small}")
<number_small> tab:            key("tab:{number_small}")
<number_small> dij:            key("delete:{number_small}")

<number_small> boot:         key("bksp:{number_small}")

<number_small> jet:     key("space:{number_small}")

pop up:      key(apps)

pinch: edit.paste()
copy: edit.copy()
cuty: edit.cut()
duplicate <number_small>:
    edit.copy()
    key("cmd-v:{number_small}")
select all:  edit.select_all()

inteli jey:  insert("intellij")
undo: edit.undo() 