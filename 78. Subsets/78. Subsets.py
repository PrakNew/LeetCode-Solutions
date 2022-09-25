class Solution:
    def subsets(self, A):
        subsets = [[]]
        for x in A:
            size = len(subsets)
            for i in range(size):
                subsets += subsets[i] + [x],
        
        return subsets
        