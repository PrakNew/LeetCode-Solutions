class Solution:
    def xorQueries(self, arr, queries):
        n = len(arr)
        prefix = [0] * (n+1)
        prefix[0] = arr[0]
        for i in range(1, n):
            prefix[i] ^= prefix[i-1] ^ arr[i]
        res = []
        for l, r in queries:
            if l>0:
                res.append(prefix[r] ^ prefix[l-1])
            else:
                res.append(prefix[r])
        return res