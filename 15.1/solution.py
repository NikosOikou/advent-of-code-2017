a = 277
b = 349
div = 2147483647
count = 0
for _ in xrange(40000000):
    a *= 16807
    a %= div

    b *= 48271
    b %= div

    if '{:016b}'.format(a)[-16:] == '{:016b}'.format(b)[-16:]:
        count += 1

print count
