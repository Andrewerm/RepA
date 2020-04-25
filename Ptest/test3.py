def cool_range(start, stop, inc):
    x = start
    while x < stop:
        yield x
        x += inc

for n in cool_range(1, 5, 0.5):
    print(n)