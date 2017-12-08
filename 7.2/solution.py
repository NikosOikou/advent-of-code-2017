# Create  weight by child and parent by child dicts
weights = {}
parent_by_child = {}

for line in open('input.txt'):
    name = line.split()[0]

    if '->' in line:
        programs = line.split('->')[1].split(',')

        for program in programs:
            parent_by_child[program.strip()] = name

    weight = int(line.split('(')[1].split(')')[0].strip())
    weights[name] = weight

starting_weights = weights.copy()

def get_children(parent):
    return [child for child in parent_by_child if parent_by_child[child] == parent]

def get_edges():
    # nodes without children and without nephews
    result = []
    for child, parent in parent_by_child.iteritems():
        include = True
        if get_children(child):
            continue
        for sibling in get_children(parent):
            if get_children(sibling):
                include = False
                break
        if include:
            result.append(child)
    return result

stop = False
while not stop:
    for child in get_edges():
        if child not in parent_by_child:
            continue

        parent = parent_by_child[child]
        children = get_children(parent)
        children_weights = [weights[c] for c in children]


        if len(set(children_weights)) == 1:
            # Simplify tree
            for c in children:
                weights[parent] += weights[c]
                del parent_by_child[c]
        else:
            # Found inbalanced parent
            stop = True
            for w in children_weights:
                if children_weights.count(w) == 1:
                    break
            for c in children:
                if weights[c] == w:
                    break

            max_weight = max(children_weights)
            min_weight = min(children_weights)

            diff = max_weight - min_weight

            if w == max_weight:
                print starting_weights[c] - diff

            else:
                print starting_weights[c] + diff

            break
