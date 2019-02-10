class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'List[int]':
        if not nums:
            return []
        
        nums = sorted(nums)
        res = []
        counter = 0
        size = len(nums)/3
        cur = nums[0]
        
        for num in nums:
            if num == cur:
                counter += 1
            else:
                if counter > size:
                    res.append(cur)
                cur = num
                counter = 1
        
        if counter > size:
            res.append(cur)
            
        return res