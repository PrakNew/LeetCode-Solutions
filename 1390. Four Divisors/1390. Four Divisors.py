'''
Time complexity : O(sqrt(n))
Space complexity: O(sqrt(n))
'''

def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            res = []
            for j in range(1, (int)(num**0.5)+1):
                if num%j==0:
                    res.append(j)
                    if j!=(num**0.5):
                        res.append((int)(num/j))
            # print(num, res)
            if len(res)==4:
                ans += sum(res)
            
        return ans