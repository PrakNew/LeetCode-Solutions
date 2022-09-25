class Solution:
    def letterCombinations(self, digits):
        
        letters = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        
        res = []
        
        def util(digits, string = ''):
            if not digits:
                res.append(string)
                return
            
            for ch in letters[int(digits[0])]:
                util(digits[1:], string + ch)
        
        util(digits)
        
        if len(res)==1:
            return []
                
        return res