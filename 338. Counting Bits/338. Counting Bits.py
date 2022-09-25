class Solution:
    def countBits(self, num):
        
        if num==0:
            return [0]
        
        if num==1:
            return [0, 1]
        
        res = [0, 1]
        
        count = 2
        
        while count<=num:
            if count&(count-1)==0:  # power of 2
                i = 0
            res.append(res[i] + 1)
            i += 1
            count+=1
        
        return res
                