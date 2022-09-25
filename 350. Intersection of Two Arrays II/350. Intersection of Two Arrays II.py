import collections

class Solution:
    def intersect(self, nums1, nums2):
        
        def solution():
            counter = collections.Counter(nums1)
            res = []
            for x in nums2:
                if counter[x]>0:
                    res += x,
                    counter[x] -= 1
            return res
        
        def followUp():
            res = []
            nums1.sort()
            nums2.sort()
            m, n = len(nums1), len(nums2)
            i, j = 0, 0
            while i<m and j<n:
                if nums1[i]==nums2[j]:
                    res.append(nums1[i])
                    i+=1
                    j+=1
                elif nums1[i] > nums2[j]:
                    j+=1
                else:
                    i+=1

            return res
        
        return solution()
        