from itertools import cycle
from collections import defaultdict

def get_corners(n):
    j = 1
    corners = [j]
    for i in range(1, n):
        j += i
        corners.append(j)
        j += i
        corners.append(j)
    return set(corners)

def right(x, y):
    return x+1, y

def rightup(x, y):
    return x+1, y+1

def up(x, y):
    return x, y+1

def upleft(x, y):
    return x-1, y+1

def left(x, y):
    return x-1, y

def leftdown(x, y):
    return x-1, y-1

def down(x, y):
    return x, y-1

def downright(x, y):
    return x+1, y-1

actions = cycle([right, up, left, down])

corners = get_corners(600)
x = 0
y = 0
n = 325489
grid = defaultdict(int)
grid[(x, y)] += 1

for i in xrange(1, n):
    if i in corners:
        go = actions.next()
    # Find next point
    x, y = go(x, y)
    value = 0
    for neighbour in (right, rightup, up, upleft, left, leftdown, down, downright):
        value += grid[neighbour(x, y)]
    grid[(x, y)] = value
    if value > n:
        break
print value


