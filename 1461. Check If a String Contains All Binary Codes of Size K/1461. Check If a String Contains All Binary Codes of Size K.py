class Solution:
    def hasAllCodes(self, s, k):
        bins = set()
        window = s[:k]
        bins.add(window)
        for i in range(1, len(s)-k+1):
            window = window[1:]
            window += s[i+k-1]
            bins.add(window)
        return len(bins)==2**k