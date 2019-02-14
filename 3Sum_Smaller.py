class Solution:
    def threeSumSmaller(self, nums: 'List[int]', target: 'int') -> 'int':
        nums.sort()
        result = 0
        size = len(nums)
        
        for i in range(size):
            left = i+1
            right = size-1
            
            while left<right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum < target:
                    result += (right - left)
                    left += 1
                else:
                    right -= 1
        
        return result