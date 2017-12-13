max_depth = int(open('input.txt').readlines()[-1].split(':')[0])
lengths = {}

for line in open('input.txt'):
    depth, range_ = map(int, line.split(':'))
    lengths[depth] = range_

found = False
delay = 0
while not found:
    caught = False
    for step in range(max_depth + 1):
        if step in lengths:
            length = lengths[step]
            if (step + delay) % (2 * length - 2) == 0:
                caught = True
                break
    if not caught:
        found = True
    else:
        delay += 1
print delay
