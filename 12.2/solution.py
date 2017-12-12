tree = {}
for line in open('input.txt'):
    root = int(line.split()[0])
    branches = [int(l.strip(',')) for l in line.split()[2:]]
    tree[root] = branches

groups = set()

for root in tree:
    seen = {root}
    old_length = 0
    while len(seen) != old_length:
        to_add = set()
        for x in seen:
            for y in tree[x]:
                if y not in seen:
                    to_add.add(y)
        old_length = len(seen)
        seen |= to_add
    group = ''.join(map(str, sorted(seen)))
    groups.add(group)

print len(groups)
