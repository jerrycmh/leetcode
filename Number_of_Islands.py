class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        counter = 0
        height = len(grid)
        width = len(grid[0])
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    counter += 1
                    self.bfs(i, j, grid)
        
        return counter
    
    def bfs(self, i, j, grid):
        height = len(grid)
        width = len(grid[0])
        
        stack = [(i, j)]
        while stack:
            i, j = stack.pop()
            grid[i][j] = 'X'
            if i+1<height and grid[i+1][j] == '1':
                stack.append((i+1,j))
            if j+1<width and grid[i][j+1] == '1':
                stack.append((i, j+1))
            if i-1>-1 and grid[i-1][j] == '1':
                stack.append((i-1, j))
            if j-1>-1 and grid[i][j-1] == '1':
                stack.append((i, j-1))
        return