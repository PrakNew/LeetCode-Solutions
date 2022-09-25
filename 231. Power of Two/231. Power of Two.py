class Solution:
    def isPowerOfTwo(self, n):
        if n==0:
            return False
        return n & (n-1) == 0
        
'''
Method 2  
'''  
# class Solution:
#     def isPowerOfTwo(self, n):
#         ct = 0 
#         while n>0:
#             ct+=1
#             n &= (n-1)
#         return ct==1
        

        