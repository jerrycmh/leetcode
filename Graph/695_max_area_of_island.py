class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        row, col = len(grid), len(grid[0])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    stack = [(i, j)]
                    area = 0
                    while stack:
                        x, y = stack.pop()
                        if grid[x][y] == 1: 
                            area += 1
                            grid[x][y] = -1
                            if x+1 < row and grid[x+1][y] == 1:
                                stack.append((x+1, y))
                            if y+1 < col and grid[x][y+1] == 1:
                                stack.append((x, y+1))
                            if x-1 >=0 and grid[x-1][y] == 1:
                                stack.append((x-1, y))
                            if y-1 >= 0 and grid[x][y-1] == 1:
                                stack.append((x, y-1))
                    result = max(result, area)
        
        return result