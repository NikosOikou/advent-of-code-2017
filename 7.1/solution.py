all_children = set()
all_nodes = set()

for line in open('input.txt'):
    all_nodes.add(line.split()[0])

    if '->' in line:
        children = line.split('->')[1].split(',')

        for c in children:
            all_children.add(c.strip())

for node in all_nodes:
    if node not in all_children:
        print node
