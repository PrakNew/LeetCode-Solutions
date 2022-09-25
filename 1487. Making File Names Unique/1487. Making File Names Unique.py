class Solution:
    def getFolderNames(self, names):
        name_dict = {}
        res = []
        
        for name in names:
            if name in name_dict:
                ct = name_dict[name]+1
                while name + '(' + str(ct) + ')' in name_dict:
                    ct += 1
                name_dict[name] = ct
                name = name + '(' + str(ct) + ')'
            name_dict[name] = 0
            res.append(name)
        
        return res