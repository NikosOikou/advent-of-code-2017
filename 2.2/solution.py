total_sum = 0
for line in open('input.txt').readlines():
    numbers = map(int,line.strip().split())
    found = False
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if i != j and x % y == 0:
                total_sum += x / y
                found = True
                break
        if found:
            break
print total_sum