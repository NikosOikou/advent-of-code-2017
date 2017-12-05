n_valid = 0
for line in open('input.txt').readlines():
    words = line.strip().split()
    if len(words) == len(set(words)):
        n_valid += 1
print n_valid