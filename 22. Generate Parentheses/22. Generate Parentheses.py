class Solution:
    def generateParenthesis(self, n: int):
        
        res = []
        
        def util(left, right, path):
            if left > 0:
                util(left - 1, right, path + '(')
            if right > left:
                util(left, right-1, path + ')')
            
            if right==0:
                res.append(path)
        
        util(n, n, '')
        return res