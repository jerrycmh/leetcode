class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        p = 1
        products = [1]*n
        
        for i in range(n):
            products[i] *= p
            p *= nums[i]
        
        p = 1
        for i in range(n-1,-1,-1):
            products[i] *= p
            p *= nums[i]
        return products