def prime():
    '''Prime sequence generator.'''

    def hexstep():
        '''Generate 6n-1, 6n+1 sequence. '''
        n   = 1
        while True:
            hex = 6*n
            yield hex-1
            yield hex+1
            n   += 1

    def isprime(n):
        for p in primes:
            if n%p==0:  return False
            if p**2>n:  return True     # p**2>n is faster than p>n**.5

    yield 2
    yield 3
    primes  = [3]   # hexstep generates odd numbers, so 2 is unneccessary
                    # this list is interal cache of calcuated primes

    for n in hexstep():    # all primes (except 2 and 3) are 6n-1 or 6n+1
        if isprime(n):
            yield n
            primes.append(n)
prime = prime()
i = 0
for p in prime:
	i = i+1
	# print p
	if(i == 10001): 
		print p
		break 



