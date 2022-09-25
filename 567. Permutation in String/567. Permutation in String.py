class Solution:
    def checkInclusion(self, s1, s2):
        mask_1 = [0] * 26
        mask_2 = [0] * 26
        
        for ch in s1:
            mask_1[ord(ch)-ord('a')] += 1
        
        for ch in s2[:len(s1)]:
            mask_2[ord(ch)-ord('a')] += 1
        
        if(mask_1==mask_2):
            return True 
        
        size = len
        
        for i in range(1, len(s2)-len(s1)+1):
            mask_2[ord(s2[i-1])-ord('a')] -= 1
            mask_2[ord(s2[i+size(s1)-1])-ord('a')] += 1
            if mask_1==mask_2:
                return True 
        
        return False