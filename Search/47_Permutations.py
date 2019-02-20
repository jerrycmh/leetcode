class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        def helper(lists, cur_list):
            if not lists:
                if cur_list not in res:
                    res.append(cur_list)
                return
            for i in xrange(len(lists)):
                helper(lists[:i]+lists[i+1:],cur_list+[lists[i]],res)
        
        def backtrack(index = 0):
            if index == len(nums):
                res.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                backtrack(index+1)
                nums[i], nums[index] = nums[index], nums[i]
        
        res = []
        backtrack()
        return res