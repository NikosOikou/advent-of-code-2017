from itertools import cycle

def n(n_col, n_row):
    return n_col, n_row + 2

def nw(n_col, n_row):
    return n_col - 1, n_row + 1

def sw(n_col, n_row):
    return n_col - 1, n_row - 1

def s(n_col, n_row):
    return n_col, n_row - 2

def se(n_col, n_row):
    return n_col + 1, n_row - 1

def ne(n_col, n_row):
    return n_col + 1, n_row + 1

n_col = 0
n_row = 0
steps = open('input.txt').read().split(',')

max_distance = 0
for step in steps:
    direction = '{}(n_col, n_row)'.format(step)
    n_col, n_row = eval(direction)

move_right = cycle([ne, se])
distance = 0
col = 0
row = 0

while col < n_col and row > n_row:
    col, row = se(col, row)
    distance += 1
if col == n_col:
    while row > n_row:
        col, row = s(col, row)
        distance += 1
elif row == n_row:
    while col < n_col:
        col, row = move_right.next()(col, row)
        distance += 1

print distance
