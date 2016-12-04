def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
fibonacci = fibonacci()

from itertools import takewhile
print sum(x for x in (takewhile(lambda x: x<4*10**6, fibonacci)) if x%2 == 0)