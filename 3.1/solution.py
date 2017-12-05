from itertools import cycle
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...

def get_corners(n):
    i = 1
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

for i in xrange(2, n+1):
    if i in corners:
        go = actions.next()
    x, y = go(x, y)
distance = abs(x) + abs(y)
print distance


