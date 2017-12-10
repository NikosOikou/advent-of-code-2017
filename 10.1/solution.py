t = range(256)
current_idx = 0
skip_size = 0
for n in map(int, open('input.txt').read().split(',')):
    sublist = []
    for i in range(n):
        idx = current_idx + i
        if idx >= 256:
            idx -= 256
        sublist.append(t[idx])
    sublist = list(reversed(sublist))
    for i in range(n):
        idx = current_idx + i
        if idx >= 256:
            idx -= 256
        t[idx] = sublist[i]
    current_idx += n + skip_size
    if current_idx >= 256:
        current_idx -= 256
    skip_size += 1

print t[0] * t[1]