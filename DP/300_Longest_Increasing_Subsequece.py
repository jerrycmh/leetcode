class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        result = [1 for _ in range(len(nums))]
        result[0] = 1
        for i in range(1, len(nums)):
            max_num = 1
            for j in range(i):
                if nums[j] < nums[i] and result[j]+1 > max_num:
                    max_num = result[j]+1
            result[i] = max_num

        return max(result)