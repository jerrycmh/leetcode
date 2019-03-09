class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return size
        lengths = [0 for _ in range(size)]
        counts = [1 for _ in range(size)]
        
        for i in range(size):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] >= lengths[i]:
                        lengths[i] = 1+lengths[j]
                        counts[i] = counts[j]
                    elif lengths[j]+1 == lengths[i]:
                        counts[i] += counts[j]
        
        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)