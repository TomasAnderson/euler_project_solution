from collections import defaultdict

def groupcount(sq):
    d = defaultdict(int)  # default 0
    for each in sq:
        d[each] += 1
    return dict(d)

def primefactors(n):
    f = 2
    while f * f <= n:
        while not n % f:
            yield f
            n //= f
        f += 1
    if n > 1:
        yield n    

def uniprimefact(n):
    return groupcount(primefactors(n))

def product(s):
    return reduce(lambda x,y:x*y, s, 1)

nums = range(1, 20)

d = {}
for i in nums:
    for (prime, power) in uniprimefact(i).items():
        if (prime in d and d[prime] < power) or (prime not in d):
            d[prime] = power 

print product(prime**power for (prime, power) in d.items())