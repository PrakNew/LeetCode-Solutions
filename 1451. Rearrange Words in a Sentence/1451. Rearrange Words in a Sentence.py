class Solution:
    def arrangeWords(self, text):
        mp = {}
        for word in text.split():
            if len(word) not in mp:
                mp[len(word)] = []
            mp[len(word)].append(word)
        
        ans = []
        for key, val in mp.items():
            ans.append([key, val])
            
        ans.sort()
        
        res = ""
        
        for item in ans:
            for string in item[1]:
                if 'A'<=string[0]<='Z':
                    string = chr(ord(string[0])+32) + string[1:]
                res += string
                res += ' '
        
        res = chr(ord(res[0])-32) + res[1:-1]
        
        return res