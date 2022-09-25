class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        
        # Find the rightmost set bit
        mask = -xor & xor
        
        first, second = 0, 0
        
        for num in nums:
            if num & mask:
                first ^= num
            else:
                second ^= num
        
        return [first, second]