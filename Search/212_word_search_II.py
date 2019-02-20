class TrieNode(object):
    def __init__(self):
        self.sons = {}
        self.word = None

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.sons: node.sons[ch] = TrieNode()
            node = node.sons[ch]
        node.word = word

class Solution(object):
    def findWords(self, board, words):

        self.res = set()
        ## step1. insert all words into trie
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ## step2. search each board starting pointer
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.search(board, i, j, trie.root)
        
        return list(self.res)
    
    def search(self, board, i, j, trienode):
        if board[i][j] not in trienode.sons: return 
        
        node = trienode.sons[board[i][j]]
        if node.word != None: self.res.add(node.word)
        
        temp = board[i][j]
        board[i][j] = '#'
        for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                self.search(board, x, y, node)
        board[i][j] = temp