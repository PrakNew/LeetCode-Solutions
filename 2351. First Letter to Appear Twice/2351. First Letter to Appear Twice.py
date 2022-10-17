
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        s1=set()
        for x in s:
            if x in s1:
                return x
            s1.add(x)