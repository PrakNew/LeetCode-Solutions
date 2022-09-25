class Solution:
    def decodeString(self, s):
        stack = []
        k = 0
        string = ''
        
        for i in range(len(s)):
            if s[i].isdigit():
                k = k*10 + int(s[i])
            elif s[i]=='[':
                stack.append(string)
                stack.append(k)
                string = ''
                k = 0
            elif s[i]==']':
                prev_k = stack.pop()
                prev_string = stack.pop()
                string =  prev_string + prev_k * string
                
            else:
                string += s[i]
            
        return string