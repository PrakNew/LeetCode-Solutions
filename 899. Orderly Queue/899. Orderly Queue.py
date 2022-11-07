# Pattern based question where we can see a pattern that if k is greater than 1 and there are infinte rotations then we will end up in sorted order only so for k==1 we just need to find the smallest one possible
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        return min(s[i:]+s[:i] for i in range(len(s))) if k==1 else ''.join(sorted(s))