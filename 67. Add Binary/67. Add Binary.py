class Solution:
    def addBinary(self, a, b):
        carry = 0
        m, n = len(a), len(b)
        i, j = m-1, n-1
        res = ''
        
        while i>=0 and j>=0:
            a_bit, b_bit = int(a[i]), int(b[j])
            ans = a_bit + b_bit + carry
            if ans<2:
                res += str(ans)
                carry = 0
            elif ans==2:
                res += '0'
                carry = 1
            else: # res == 3
                res += '1'
                carry = 1
            i-=1
            j-=1
        
        while i>=0:
            a_bit = int(a[i])
            ans = a_bit + carry
            if ans<2:
                res += str(ans)
                carry = 0
            else: # ans ==2
                res += '0'
                carry = 1
            i-=1
        
        while j>=0:
            b_bit = int(b[j])
            ans = b_bit + carry
            if ans<2:
                res += str(ans)
                carry = 0
            else: # ans ==2
                res += '0'
                carry = 1
            j-=1
        
        if carry==1:
            res += '1'
            
        return res[::-1]
                