class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()
        
    def findValid(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return (row, col)
        return (-1, -1)
    
    def solve(self):
        row, col = self.findValid()
        if row == -1 and col == -1:
            return True
        for num in ['1','2','3','4','5','6','7','8','9']:
            if self.checkSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = '.'
        return False
    
    def checkSafe(self, row, col, num):
        for t_col in range(9):
            if self.board[row][t_col] == num: return False
        for t_row in range(9):
            if self.board[t_row][col] == num: return False
        box_c = col-col%3
        box_r = row-row%3
        for r in range(box_r, box_r+3):
            for c in range(box_c, box_c+3):
                if self.board[r][c] == num:
                    return False
        
        return True