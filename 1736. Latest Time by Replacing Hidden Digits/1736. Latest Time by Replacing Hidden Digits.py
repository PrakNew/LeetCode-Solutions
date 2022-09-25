"""
Time complexity : O(1)
Space complexity: O(1)
"""
class Solution:
    def maximumTime(self, time):
        res = ''
        if time[0] == '?':
            if time[1] in ['?', '0', '1', '2', '3']:
                res += '2'
            else:
                res += '1'
        else:
            res += time[0]
                
        res += ''
        
        if time[1] == '?':
            if res[-1] in ['0', '1']:
                res += '9'
            else:
                res += '3'
        else:
            res += time[1]
        
        res += ':'
        
        res += '5' if time[3] == '?' else time[3]
        
        res += '9' if time[4] == '?' else time[4]
            
        return res