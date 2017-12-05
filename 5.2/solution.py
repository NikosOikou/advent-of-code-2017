instructions = [int(line.strip()) for line in open('input.txt').readlines()]
state = {i: n for i, n in enumerate(instructions)}
position = 0
count = 0
while True:
    count += 1
    old_position = position
    offset = state[position]
    position += offset
    if position in state:
        if offset >= 3:
            state[old_position] -= 1
        else:
            state[old_position] += 1
    else:
        break
print count
