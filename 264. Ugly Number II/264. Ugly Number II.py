class Solution:
    def nthUglyNumber(self, n):
        if n==1:
            return n
        
        ugly = [1]
        next_mul_2 = 2
        next_mul_3 = 3
        next_mul_5 = 5
        i2, i3, i5 = 0, 0, 0
        
        for i in range(1, n):
            next_mul = min(next_mul_2, next_mul_3, next_mul_5)
            ugly.append(next_mul)

            if next_mul == next_mul_2:
                i2 += 1
                next_mul_2 = ugly[i2] * 2

            if next_mul == next_mul_3:
                i3 += 1
                next_mul_3 = ugly[i3] * 3

            if next_mul == next_mul_5:
                i5 += 1
                next_mul_5 = ugly[i5] * 5
        
        return next_mul
        