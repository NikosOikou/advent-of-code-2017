total_sum = 0
for line in open('input.txt').readlines():
    numbers = map(int,line.strip().split())
    found = False
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if i != j:
                d = divmod(x, y)
                if d[1] == 0:
                    total_sum += d[0]
                    found = True
                    break
        if found:
            break
print total_sum