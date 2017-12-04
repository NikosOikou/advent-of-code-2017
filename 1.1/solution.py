n = open('input.txt').read().strip()

n += n[0]

total_sum = 0
for i, digit in enumerate(n[:-1]):
    digit = int(digit)
    next_digit = int(n[i+1])
    print digit, next_digit
    if digit == next_digit:
        total_sum += digit
print total_sum