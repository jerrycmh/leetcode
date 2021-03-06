class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_one = self.helper(nums[1:])
        max_two = self.helper(nums[0:-1])
        return max(max_one, max_two)
    
    def helper(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        result = [0] * len(nums)
        result[0] = nums[0]
        result[1] = nums[1]
        
        for i in range(2, len(nums)):
            if i == 2:
                result[i] = nums[i] + nums[i-2]
            else:
                result[i] = max(nums[i]+result[i-2], nums[i]+result[i-3])        
        
        
        return max(result[-1], result[-2])