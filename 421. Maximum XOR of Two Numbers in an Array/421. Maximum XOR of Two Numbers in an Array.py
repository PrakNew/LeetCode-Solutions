'''
Idea: Bitwise Trie

Time complexity : O(n)
Space complexity: O(1)
'''

class Solution:
    def findMaximumXOR(self, A):
        L = len(bin(max(A))) - 2
        
        # left pad every number until L digits
        A = [[(num>>i)&1 for i in range(L-1, -1, -1)] for num in A]
        
        trie_node = {}
        max_xor = 0
        for num in A:
            node = trie_node
            xor_node = trie_node
            curr_xor = 0
            for bit in num:
                # insert new bit into trie
                if bit not in node:
                    node[bit] = {}
                
                node = node[bit]
                
                # to compute max xor of the number
                toggled_bit = 1 - bit 
                
                if toggled_bit in xor_node:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    curr_xor = curr_xor << 1
                    xor_node = xor_node[bit]
            
            max_xor = max(max_xor, curr_xor)
        
        return max_xor
                    
                