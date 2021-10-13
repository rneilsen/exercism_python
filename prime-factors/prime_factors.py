def factors(value):
    primes = []
    n = 1

    prime_factors = []
    remainder = value
    while remainder > 1:
        n += 1

        # test if n is prime using current known primes
        n_prime = True
        for p in primes:
            if n % p == 0:
                n_prime = False
                break
            if p*p > n:
                # no need to keep testing primes once we pass sqrt(n)
                break
        
        if n_prime:
            primes.append(n)
            
            while remainder % n == 0:
                prime_factors.append(n)
                remainder = remainder // n
    
    return prime_factors
