'''
Time complexity : O(n) for n shift queries
Space complexity: O(1)
'''

def stringShift(self, s, shift):
    index = 0
    n = len(s)
    for direction, amount in shift:
        if direction==0: # left shift
            if index + amount >= n:
                amount -= n - index
                index = 0 + amount
            else:
                index += amount
            
        elif direction==1:  # right shift
            if index >= amount:
                index -= amount
            else:
                amount -= (index-0)
                index = n - amount
    
    return s[index:] + s[:index]