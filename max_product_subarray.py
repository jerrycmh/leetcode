class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        
        top = low = result
        
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur < 0:
                top, low = low, top
            
            top = max(cur, cur*top)
            low = min(cur, cur*low)
            
            result = max(result, top)
        
        return result