import heapq
class Solution:
    def nthUglyNumber(self, n: 'int') -> 'int':
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        heap = [2, 3, 5]
        for _ in range(2, n):
            num = heapq.heappop(heap)
            if num*2 not in heap:
                heapq.heappush(heap, num*2)
            if num*3 not in heap:
                heapq.heappush(heap, num*3)
            if num*5 not in heap:
                heapq.heappush(heap, num*5)
            
        return heap[0]