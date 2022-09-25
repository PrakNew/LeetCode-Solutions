class Solution:
    def canBeEqual(self, target, arr):
        for num in target:
            if num not in arr:
                return False
        
        return True
        
        