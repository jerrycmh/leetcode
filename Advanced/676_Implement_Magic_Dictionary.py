class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.trie.insert(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        return self.trie.search(word)

class Trie():
    
    def __init__(self):
        self.root = {}
        self.END = ()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[self.END] = True
    
    def search(self, word):
        stack = [(self.root, 0, 0)]
        
        while stack:
            node, index, diff = stack.pop()
            if index == len(word):
                if diff == 1 and self.END in node:
                    return True
                else: continue
            if word[index] in node:
                stack.append((node[word[index]], index+1, diff))
            if diff == 1:
                continue
            for key, value in node.items():
                if key != self.END and key != word[index]:
                    stack.append((value, index+1, diff+1))
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)