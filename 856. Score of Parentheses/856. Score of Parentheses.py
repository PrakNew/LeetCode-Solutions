"""
Idea: Stack

Time complexity: O(n)
Space complexity: O(1)
"""

import collections

class Solution:
    def scoreOfParentheses(self, S):
        
        def constantSpace():
            n = len(S)
            core = 0
            res = 0
            for i, ch in enumerate(S):
                if ch == '(':
                    core += 1
                else:
                    core -= 1
                    if S[i-1] == '(':
                        res += 1 << core

            return res
        
        
        def linearSpace():
            st = collections.deque([0])
            for ch in S:
                if ch == '(':
                    st += 0,
                else:
                    pop = st.pop()
                    level = st.pop()
                    st += level + max(2 * pop, 1),
            
            return st[-1]
        
        return constantSpace()
        return linearSpace()