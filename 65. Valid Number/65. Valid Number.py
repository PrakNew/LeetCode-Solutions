# easy find the float and thats all
class Solution:
    def isNumber(self, s: str) -> bool:
        try:float(s);return 'inf' not in s.lower()
        except:return False
