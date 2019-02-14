class Solution:
    def missingNumber(self, nums: 'List[int]') -> 'int':
        size = len(nums)+1
        total = (0+size-1)*size//2
        
        for n in nums:
            total -= n
        
        return total