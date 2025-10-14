# Delete Commands Analysis

## Current Configuration (Your Setup)

### Simple Delete Commands
Located in `/core/keys/mac/special_key.talon-list`:
```
delete: delete
dij: delete
```
Both send a single delete key press.

### Numbered Delete Command
Located in `/core/keys/keystroke.talon`:
```
<number_small> dij: key("delete:{number_small}")
```
Allows commands like "5 dij" to delete 5 characters.

## Community Version (Upstream)

### Compound Command System
Main grammar in `/core/edit/edit.talon`:
```
<user.edit_action> <user.edit_modifier>: user.edit_command(edit_action, edit_modifier)
```

### Actions
From `/core/edit/edit_command_actions.talon-list`:
```
clear: delete
```

### Modifiers
From `/core/edit/edit_command_modifiers_repeatable.talon-list`:
```
right: right
left: left
word: word
word left: wordLeft
word right: wordRight
```

### Examples
- `clear 5 right` - delete 5 characters to the right
- `clear word` - delete current word
- `clear line` - delete current line

## Key Differences
- Your setup: Simple numbered repetition (`5 dij`)
- Community: Flexible compound system (`clear 5 right`, `clear word`, etc.)
- Community system is more expressive but potentially more complex vocabulary
