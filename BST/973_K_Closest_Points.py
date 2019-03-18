import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points: return []
        heap = []
        for x, y in points:
            dis = x**2+y**2
            if not heap or len(heap) < K:
                heapq.heappush(heap, [-dis, [x, y]])
            else:
                if -dis > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [-dis, [x, y]])
        
        result = [point for _, point in heap]
        return result