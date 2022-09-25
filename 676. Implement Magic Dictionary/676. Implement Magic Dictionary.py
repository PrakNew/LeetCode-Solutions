import collections

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
    
    def getNeighbors(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i+1:]
        

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        self.words = set(dict)
        self.counter = collections.Counter(nei for word in self.words for nei in self.getNeighbors(word))
        

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for nei in self.getNeighbors(word):
            if self.counter[nei] > 1 or self.counter[nei]==1 and word not in self.words:
                return True
        
        return False
