class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        visited = {}
        while N:
            c = tuple(cells)
            if c in visited:
                N %= visited[c] - N
            visited[c] = N
            
            if N >= 1:
                N -= 1
                cells = [int(i >0 and i<7 and cells[i-1] == cells[i+1]) for i in range(8)]
        
        return cells