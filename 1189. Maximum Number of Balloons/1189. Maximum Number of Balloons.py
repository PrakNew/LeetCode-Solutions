class Solution:
    def maxNumberOfBalloons(self, text):
        freq = [0] * 26
        for ch in text:
            freq[ord(ch)-ord('a')] += 1
        
        # b, a, l, l, o, o, n
        return min(freq[1], freq[0], freq[11]>>1, freq[14]>>1, freq[13])
        