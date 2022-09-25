"""
Idea: Minimax algorithm
"""

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist, master):
        
        def match(w1, w2):
            return sum(i==j for i, j in zip(w1, w2))            # number of matching characters in corresponding positions
        
        score = 0
        while score < 6:
            count = [collections.Counter(w[i] for w in wordlist) for i in range(6)]        
            best_guess = max(wordlist, key = lambda word: sum(count[i][c] for i, c in enumerate(word)))
            score = master.guess(best_guess)
            wordlist = [w for w in wordlist if match(w, best_guess) == score]
        
            
            