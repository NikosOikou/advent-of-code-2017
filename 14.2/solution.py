def is_used(p):
    x, y = p
    if x < 0 or x > 127 or y < 0 or y > 127:
        return False
    return grid.split()[y][x] == '1'

def up(p):
    x, y = p
    return (x, y-1)

def down(p):
    x, y = p
    return (x, y+1)

def left(p):
    x, y = p
    return (x-1, y)

def right(p):
    x, y = p
    return (x+1, y)

def expand(p, group):
    for direction in [up, down, left, right]:
        nbr = direction(p)
        if is_used(nbr) and nbr not in seen:
            group.add(nbr)
            seen.add(nbr)
            expand(nbr, group)

def knot_hash(s):
    chars = map(ord, s)
    chars += [17, 31, 73, 47, 23]
    chars *= 64
    t = range(256)
    current_idx = 0
    skip_size = 0

    for n in chars:
        sublist = []
        for i in range(n):
            idx = current_idx + i
            idx = idx % 256
            sublist.append(t[idx])
        sublist = list(reversed(sublist))
        for i in range(n):
            idx = current_idx + i
            idx = idx % 256
            t[idx] = sublist[i]
        current_idx += n + skip_size
        current_idx = current_idx % 256
        skip_size += 1

    result = []
    for i in range(16):
        next_sixteen = t[16*i: 16*(i+1)]
        r = reduce(lambda x, y: x ^ y, next_sixteen)
        result.append(r)
    return ''.join(['{:02x}'.format(x) for x in result])

r = 'hxtvlmkl'
grid = ''
for i in range(128):
    knot = knot_hash('%s-%s' % (r, i))
    bits = '{:0128b}'.format(int(knot, base=16))
    grid += bits + '\n'

seen = set()
groups = []
for y, row in enumerate(grid.split()):
    for x, value in enumerate(row):
        p = (x, y)
        if is_used(p) and p not in seen:
            group = {p}
            seen.add(p)
            expand(p, group)
            groups.append(group)
print len(groups)