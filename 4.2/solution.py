n_valid = 0
for line in open('input.txt').readlines():
    words = line.strip().split()
    anagramed_sorted = [''.join(sorted(word)) for word in words]
    if len(words) == len(set(anagramed_sorted)):
        n_valid += 1
print n_valid