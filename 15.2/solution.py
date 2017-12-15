a = 277
b = 349
div = 2147483647
values_a = []
values_b = []
size = 5000000
while len(values_a) < size or len(values_b) < size:
    a *= 16807
    a %= div
    if a % 4 == 0:
        values_a.append(a)

    b *= 48271
    b %= div
    if b % 8 == 0:
        values_b.append(b)

count = 0
for a, b in zip(values_a, values_b):
    if '{:016b}'.format(a)[-16:] == '{:016b}'.format(b)[-16:]:
        count += 1

print count
