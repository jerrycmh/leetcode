class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if upper == lower:
                return [str(upper)]
            else:
                return [str(lower)+"->"+str(upper)]
        
        result = []
        if lower < nums[0]:
            if lower == nums[0]-1:
                result.append(str(lower))
            else:
                result.append(str(lower)+"->"+str(nums[0]-1))
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 2:
                result.append(str(nums[i]-1))
            elif nums[i] - nums[i-1] > 2:
                result.append(str(nums[i-1]+1)+"->"+str(nums[i]-1))
        
        if upper > nums[-1]:
            if upper == nums[-1]+1:
                result.append(str(upper))
            else:
                result.append(str(nums[-1]+1)+"->"+str(upper))
        
        return result