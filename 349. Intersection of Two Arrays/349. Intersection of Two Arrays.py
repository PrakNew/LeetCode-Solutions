class Solution:
    def intersection(self, nums1, nums2):
        def setTheory():
            set1 = set(nums1)
            set2 = set(nums2)
            return list(set1 & set2)
        
        def sortedArray():
            nums1.sort()
            nums2.sort()
            i, j, m, n = 0, 0, len(nums1), len(nums2)
            res = []
            while i<m and j<n:
                left, right = nums1[i], nums2[j]
                if left==right:
                    res.append(left)
                    while i<m and left==nums1[i]:
                        i+=1
                    while j<n and right==nums2[j]:
                        j+=1
                elif left < right:
                    while i<m and left==nums1[i]:
                        i+=1
                else:
                    while j<n and right==nums2[j]:
                        j+=1
            return res
        
        return sortedArray()
        return setTheory()
                