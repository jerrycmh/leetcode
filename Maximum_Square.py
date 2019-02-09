class Solution:
    def maximalSquare(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix:
            return 0
        
        max_area = 0
        
        res = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            res[i][0] = int(matrix[i][0])
            max_area = max(res[i][0], max_area)
        for j in range(len(matrix[0])):
            res[0][j] = int(matrix[0][j])
            max_area = max(res[0][j], max_area)

        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "1":
                    res[i][j] = min(res[i-1][j], res[i][j-1], res[i-1][j-1])+1
                    max_area = max(res[i][j], max_area)
                else:
                    res[i][j] = 0
        
        return max_area**2