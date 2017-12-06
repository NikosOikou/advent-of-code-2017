from itertools import cycle

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

def up(x, y):
    return x, y+1

def left(x, y):
    return x-1, y

def down(x, y):
    return x, y-1

actions = cycle([right, up, left, down])

corners = get_corners(600)
x = 0
y = 0
n = 325489

for i in xrange(1, n):
    if i in corners:
        go = actions.next()
    # Find next point
    x, y = go(x, y)
distance = abs(x) + abs(y)
print distance


