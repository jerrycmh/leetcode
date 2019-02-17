class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        tree = self.tree
        size = len(word)
        index = 0
        while index != size:
            char = word[index]
            if char in tree:
                if index == size-1:
                    tree[char][1] = True
                tree = tree[char][0]
            else:
                break
            index += 1
        
        for i in range(index, size):
            char = word[i]
            bol = False
            if i == size-1:
                bol = True
            tree[char] = [{}, bol]
            tree = tree[char][0]

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tree = self.tree
        for i, char in enumerate(word):
            if char in tree:
                if i == len(word)-1:
                    return tree[char][1]
                tree = tree[char][0]
            else:
                return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tree = self.tree
        for char in prefix:
            if char in tree:
                tree = tree[char][0]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
