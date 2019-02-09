class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        if not nums:
            return 0
        nums = sorted(nums)[::-1]
        return nums[k-1]


    ## Heap Solution
    import heapq
	def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
    if not nums or k > len(nums):
        return -1
    
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, nums[i])
    
    return min_heap[0]