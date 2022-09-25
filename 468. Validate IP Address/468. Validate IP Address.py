class Solution:
    def validIPAddress(self, IP):
        if IP == "":
            return "Neither"
        
        numbers = set(str(i) for i in range(10))
        letters = set(['a','b','c','d','e','f','A','B','C','D','E','F'])
        validIPv4 = set(str(i) for i in range(256))
        
        def validIPv6(hexa):
            if len(hexa)>4:
                return False
            elif 1<=len(hexa)<=4:
                for i in range(len(hexa)):
                    if hexa[i] not in (numbers | letters):
                        return False
            elif len(hexa)==0:
                return False
            return True
        
        if IP[-1] in set(['.', ':']):
            return "Neither"

        if '.' in IP: # IPv4 address
            i = 0
            res = ""
            decimal = 0
            while i < len(IP):
                while i < len(IP) and IP[i] != '.':
                    res += IP[i]
                    i+=1
                if res in validIPv4:
                    decimal += 1
                    res = ""
                    i+=1
                else:
                    return "Neither"
            if decimal==4:
                return "IPv4"
            return "Neither"
        
        else: # IPv6 address
            i = 0
            res = ""
            hexadecimal = 0
            while i < len(IP):
                while i < len(IP) and IP[i]!=':':
                    res += IP[i]
                    i += 1
                if validIPv6(res):
                    hexadecimal += 1
                    res = ""
                    i += 1
                else:
                    return "Neither"
            if hexadecimal==8:
                return "IPv6"
            return "Neither"
            