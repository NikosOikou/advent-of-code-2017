score = 0
amount = 0
is_garbage = False
ignore_next = False

for c in open('input.txt').read():
    if ignore_next:
        ignore_next = False
        continue
    if not is_garbage and c == '{':
        amount += 1
        score += amount
    elif c == '<':
        is_garbage = True
    elif c == '!' and is_garbage:
        ignore_next = True
    elif c == '>':
        is_garbage = False
    elif not is_garbage and c == '}':
        amount -= 1

print score