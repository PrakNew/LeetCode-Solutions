class Solution:
    def maxArea(self, h, w, hCuts, vCuts):
        hCuts.sort()
        vCuts.sort()
        
        max_h = max(hCuts[0], h - hCuts[-1])
        max_v = max(vCuts[0], w - vCuts[-1])
        
        for i in range(1, len(hCuts)):
            max_h = max(max_h, hCuts[i] - hCuts[i-1])
        
        for i in range(1, len(vCuts)):
            max_v = max(max_v, vCuts[i] - vCuts[i-1])
        
        return (max_h * max_v) % (10**9+7)
        
    