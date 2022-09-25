class Solution:
    def simplifiedFractions(self, n) :
        res = {}
        
        for den in range(2, n+1):
            for num in range(1, den):
                if num/den not in res:
                    res[num/den] = []
                res[num/den].append(str(num) + "/" + str(den))
                # res.append(str(num) + "/" + str(den))
        
        ans = []
        for key, val in res.items():
            ans.append(val[0])
        
        return ans