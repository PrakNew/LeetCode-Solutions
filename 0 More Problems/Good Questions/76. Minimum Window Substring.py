''' What I have done here is created a used 2 pointers for solving the question 
1 take the right pointer to the point where all the elements are included of string2 i.e its length will become zero
2 now move the left pointer to the point where again the string can be formed
3 always check for the min length of (right-left+1)
'''
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counter = collections.Counter(t)
        left = 0
        substring = ""
        target_length = len(t)
        
        for right in range(len(s)):
            # if we find a letter in t
            if target_counter[s[right]] > 0:
                target_length -= 1
            
            target_counter[s[right]] -= 1
            print(left,right,target_counter,target_length)
            # if the sliding window is valid, i.e. we find all letters in t
            while target_length == 0:
                len_window = right - left + 1
                
                if not substring or len(substring) > len_window:
                    substring = s[left: right + 1]
                
                # move the window one step to the right
                target_counter[s[left]] += 1
                
                # if s[left] is a letter in t
                # we need to break the while loop
                if target_counter[s[left]] > 0:
                    target_length += 1
                
                left += 1
        print(left,target_counter)
        return substring
