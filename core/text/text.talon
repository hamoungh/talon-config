# Minimal formatter grammar: prose, code, and single-word formatting only

{user.prose_formatter} <user.prose>$: user.insert_formatted(prose, prose_formatter)
{user.prose_formatter} <user.prose> {user.phrase_ender}:
    user.insert_formatted(prose, prose_formatter)
    insert(phrase_ender)

<user.format_code>+$: user.insert_many(format_code_list)
<user.format_code>+ {user.phrase_ender}:
    user.insert_many(format_code_list)
    insert(phrase_ender)

{user.word_formatter} <user.word>: user.insert_formatted(word, word_formatter)


