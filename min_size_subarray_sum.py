class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)+1
        left = 0
        min_sum = 0
        
        for right in range(len(nums)):
            min_sum += nums[right]
            while min_sum >= s:
                result = min(result, right-left+1)
                min_sum -= nums[left]
                left += 1
        if result > len(nums):
            return 0
        else:
            return result
            