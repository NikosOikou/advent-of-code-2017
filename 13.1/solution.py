max_depth = int(open('input.txt').readlines()[-1].split(':')[0])
lengths = {}

for line in open('input.txt'):
    depth, range_ = map(int, line.split(':'))
    lengths[depth] = range_
    
severity = 0
for step in range(max_depth):
    if step in lengths:
        l = lengths[step]
        if step % (2 * l - 2) == 0:
            severity += step * l

print severity
