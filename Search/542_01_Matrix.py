class Solution:
    def updateMatrix(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        height = len(matrix)
        width = len(matrix[0])
        queue = []
        for i in range(height):
            for j in range(width):
                if matrix[i][j] != 0:
                    queue = [[(i,j), 0]]
                    while queue:
                        node = queue.pop(0)
                        row, col = node[0]
                        depth = node[1]
                        if matrix[row][col] == 0:
                            matrix[i][j] = depth
                            break
                        else:
                            if row > 0: queue.append([(row-1, col), depth+1])
                            if col > 0: queue.append([(row, col-1), depth+1])
                            if row < height-1: queue.append([(row+1, col), depth+1])
                            if col < width-1: queue.append([(row, col+1), depth+1])
                        
        
        return matrix