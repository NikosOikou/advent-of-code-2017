n = open('input.txt').read().strip()
l = len(n)
h = l / 2
n += n
total_sum = 0
for i, digit in enumerate(n[:l]):
    digit = int(digit)
    next_digit = int(n[i+h])
    if digit == next_digit:
        total_sum += digit
print total_sum