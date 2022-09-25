"""
Idea: Two pointers

Time complexity : O(nlogn)
Space complexity: O(1)
"""

class Solution:
    def numRescueBoats(self, people, limit):
        n = len(people)
        people.sort(reverse = True)
        i, j = 0, n - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
                
        return i