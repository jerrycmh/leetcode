import heapq
class Solution:
    def getSkyline(self, buildings: 'List[List[int]]') -> 'List[List[int]]':
        if not buildings:
            return []
        
        points = [(l, -h, r) for l, r, h in buildings] + list({(r, 0, 0) for _, r, _ in buildings})
        points = sorted(points)
        
        res = [[0, 0]]
        heap = [(0, float('inf'))]
        
        for l, neg_h, r in points:
            while l >= heap[0][1]:
                heapq.heappop(heap)
            
            if neg_h != 0:
                heapq.heappush(heap, (neg_h, r))
            
            if res[-1][1] != -heap[0][0]:
                res.append([l, -heap[0][0]])
        
        return res[1:]