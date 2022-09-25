class Solution:
    def nthSuperUglyNumber(self, n, primes):
        if n==1:
            return n
        
        ugly = [1]
        next_muls = primes[::]
        indices = [0] * len(primes)
        
        for i in range(1, n):
            next_mul = min(next_muls)
            ugly.append(next_mul)
            
            for k in range(len(primes)):
                if next_mul == next_muls[k]:
                    indices[k] += 1
                    next_muls[k] = ugly[indices[k]] * primes[k]
        
        return next_mul
            
        
            