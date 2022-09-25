"""
Idea: HashMap

Time complexity: O(m*n)
Space complexity: O(m*n)
"""

class Solution:
    def expressiveWords(self, S, words):
        
        def encode(word):
            code = []
            ct = 0
            for i in range(len(word)):
                if i > 0 and word[i] != word[i-1]:
                    code += word[i-1],
                    code += ct,
                    ct = 1
                else:
                    ct += 1
            
            if word:
                code += word[-1],
                code += ct,
            return code 
        
        def stretchy(code):
            if len(code) != code_len:
                return False 
            
            for i in range(1, code_len, 2):
                if code[i-1] != secret_code[i-1] or (secret_code[i] <= 2 and code[i] != secret_code[i]) or (secret_code[i] < code[i]):
                    return False
            
            return True
        
        res = 0
        secret_code = encode(S)
        code_len = len(secret_code)
        
        for word in words:
            if stretchy(encode(word)):
                res += 1
        
        return res