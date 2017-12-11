chars = map(ord, open('input.txt').read())
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

print ''.join(map(lambda x: x[2:], map(hex, result)))
