class Solution:
    def removeKdigits(self, num, k):
        
        ct = 0
        
        if k==len(num):
            return "0"
        
        for _ in range(k):
            removed = False
            
            while len(num)>1 and num[0]=='0':
                num = num[1:]
            
            for i in range(len(num)-1):
                if int(num[i])>int(num[i+1]):
                    removed = True
                    num = num[:i] + num[i+1:]
                    break
            
            if not removed:
                num = num[:-1]
            
            # print(num)
        
        while len(num)>1 and num[0]=='0':
                num = num[1:]
                
        return num