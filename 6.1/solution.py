banks = map(int, open('input.txt').read().strip().split())
states_seen = set()
n_banks = len(banks)
count = 0
while True:
    count += 1
    n_to_allocate = max(banks)
    idx = banks.index(n_to_allocate)
    for i in range(n_to_allocate):
        if i == 0:
            banks[idx] = 0
        idx += 1
        if idx > n_banks - 1:
            idx = 0
        banks[idx] += 1
    state = str(banks)
    if state in states_seen:
        break
    states_seen.add(state)
print count
