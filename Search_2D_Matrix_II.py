class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        tot_rows = len(matrix)
        if not tot_rows:
            return False
        
        tot_cols = len(matrix[0])
        i,j = 0, tot_cols-1
        while tot_cols:
            if matrix[i][j] == target:
                return True
            
            if target > matrix[i][j]:
                i += 1

            if i > tot_rows-1:
                return False
            
            if target < matrix[i][j]:
                j -= 1
            
            if j < 0:
                return False
        
        return False