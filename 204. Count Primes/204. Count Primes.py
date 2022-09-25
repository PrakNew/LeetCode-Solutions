class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0
        
        isPrimes = [True] * n
        primes = []
        
        def sieve(n):
            maxN = n
            isPrimes[0] = isPrimes[1] = False
            for i in range(3, maxN, 2):
                if isPrimes[i]:
                    for p in range(i*i, maxN, i):
                        if isPrimes[p]:
                            isPrimes[p] = False
            if maxN>2:
                primes.append(2)
                
            for i in range(3, maxN, 2):
                if isPrimes[i]:
                    primes.append(i)
                
        sieve(n)
        
        return len(primes)