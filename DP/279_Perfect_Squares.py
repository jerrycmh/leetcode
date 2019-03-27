class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        
        res = [float('inf') for _ in range(n+1)]
        for num in squares: res[num] = 1
        
        for i in range(1,n+1):
            if res[i] != 1:
                j = 0
                while j < len(squares) and squares[j] < i:
                    res[i] = min(res[i], res[i-squares[j]]+1)
                    j += 1
        return res[-1]