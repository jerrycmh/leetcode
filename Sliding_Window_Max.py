import heapq
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        if not nums:
            return []
        
        res = []
        cur_max = nums[0]
        index = 0
        heap = [[-nums[0], 0]]
        
        for i in range(k):
            cur_max = max(cur_max, nums[i])
            if cur_max == nums[i]:
                index = i
            heapq.heappush(heap, [-nums[i], i])
        
        res.append(cur_max)
        
        for i in range(k, len(nums)):
            heapq.heappush(heap, [-nums[i], i])
            if i - index > k-1:
                while i - index > k-1:
                    neg_val, index = heapq.heappop(heap)
                cur_max = -neg_val
            else:
                cur_max = max(cur_max, nums[i])
                if cur_max == nums[i]:
                    index = i
            res.append(cur_max)
        
        return res