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

total = 0
r = 'hxtvlmkl'
for i in range(128):
    knot = knot_hash('%s-%s' % (r, i))
    total += '{:0128b}'.format(int(knot, base=16)).count('1')

print total