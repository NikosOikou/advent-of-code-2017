total_sum = 0
for line in open('input.txt').readlines():
    numbers = map(int,line.strip().split())
    diff = max(numbers) - min(numbers)
    total_sum += diff
print total_sum