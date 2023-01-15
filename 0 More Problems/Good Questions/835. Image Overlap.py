#Data Science method
import numpy as np
from scipy import signal
def largestOverlap( img1, img2):
    n = len(img1)
    img1 = np.flip(np.flip(img1, 0), 1)   
    bigImg = np.zeros((n * 3, n * 3))  
    bigImg[n : 2 * n, n : 2 * n] = img2

    return int(np.max(signal.convolve2d(bigImg, img1)))

# What I have done is finded out all the available 1 in both the images and checked the pattern
# the pattern of (x2-x1,y2-y1) would be coinciding for multiple points so we just need
# to find out the max coinciding points in our loop 
# Complexity = O(n^4)
# Space complexity = O(number of unique coordinates)

from collections import defaultdict
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        d=defaultdict(int)
        maxc=0
        for x1 in range(n):
            for y1 in range(n):
                if img1[x1][y1]==1:
                    for x2 in range(n):
                        for y2 in range(n):
                            if img2[x2][y2]==1:
                                diff=((x2-x1),(y2-y1))                    
                                d[diff]+=1
                                maxc=max(maxc,d[diff])
        #print(d)
        return maxc


# using cartesian product same as above but a little faster
from collections import defaultdict
import itertools
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        d=defaultdict(int)
        maxc=0
        for x1, y1 in itertools.product(range(n), range(n)):
            if img1[x1][y1]==1:
                for x2, y2 in itertools.product(range(n), range(n)):
                    if img2[x2][y2]==1:
                        diff=((x2-x1),(y2-y1))                    
                        d[diff]+=1
                        maxc=max(maxc,d[diff])
        #print(d)
        return maxc