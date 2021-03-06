def primefactors(n):
    f = 2
    while f * f <= n:
        while not n%f:
            yield f
            n //= f
        f += 1
    if n > 1:
        yield n

print max(primefactors(600851475143))
