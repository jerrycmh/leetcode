class Solution:
    def summaryRanges(self, nums: 'List[int]') -> 'List[str]':
        if not nums:
            return []
        
        res = []
        start = nums[0]
        ite = start + 1
        
        for i in range(1, len(nums)):
            if nums[i] != ite:
                if ite == start + 1:
                    res.append(str(start))
                else:
                    res.append(str(start)+"->"+str(ite-1))
                start = nums[i]
                ite = start + 1
            else:
                ite += 1
        
        if ite == start + 1:
            res.append(str(start))
        else:
            res.append(str(start)+"->"+str(ite-1))
        return res