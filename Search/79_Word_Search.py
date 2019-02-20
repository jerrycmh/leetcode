class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        if not board and not word:
            return True
        if not board and word:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(i, j, board, word):
                    return True
        return False
    
    def helper(self, i, j, board, word):
        if len(word) == 0:
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[0]:
            return False
        ch = word[0]
        board[i][j] = '#'
        result = self.helper(i+1,j,board,word[1:]) or self.helper(i,j+1,board,word[1:]) or self.helper(i-1,j,board,word[1:]) or self.helper(i,j-1,board,word[1:])
        board[i][j] = ch
        return result