Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie()
        
        for weight, word in enumerate(words):
            word += "#"
            for i in xrange(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in xrange(i, 2*len(word)-1):
                    cur = cur[word[j%len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        cur = self.trie
        fix = suffix + "#" + prefix
        for letter in fix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]s