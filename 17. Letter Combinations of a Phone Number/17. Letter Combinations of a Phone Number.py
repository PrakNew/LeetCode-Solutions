from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:return []
        d={
            "2":list('abc'),
            "3":list('def'),
            "4":list('ghi'),
            "5":list('jkl'),
            "6":list('mno'),
            "7":list('pqrs'),
            "8":list('tuv'),
            "9":list('wxyz')
        }
        l = [d[x] for x in digits]
        z=list(product(*l))
        z=list(map(lambda x:''.join(x),z))
        return z
        #method 2
        def dfs(ind,prev):
            k=d[digits[ind]]
            if ind==len(digits)-1:
                for x in k:
                    abc.append(prev+x)
            else:
                for x in k:
                    dfs(ind+1,prev+x)
        dfs(0,'')
        return abc


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

        return [] if len(res)==1 else res