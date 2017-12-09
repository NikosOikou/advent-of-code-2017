is_garbage = False
ignore_next = False
n_garbage_chars = 0

for c in open('input.txt').read():
    if is_garbage:
        if c == '!' and not ignore_next:
            pass
        elif ignore_next:
            pass
        elif c == '>':
            pass
        else:
            n_garbage_chars += 1

    if ignore_next:
        ignore_next = False
        continue
    if c == '<':
        is_garbage = True
    elif c == '!' and is_garbage:
        ignore_next = True
    elif c == '>':
        is_garbage = False

print n_garbage_chars
