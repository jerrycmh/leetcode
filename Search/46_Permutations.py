class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        def helper(lists, cur_list, res):
            if not lists:
                if cur_list not in res:
                    res.append(cur_list)
                return
            for i in xrange(len(lists)):
                helper(lists[:i]+lists[i+1:],cur_list+[lists[i]],res)
        
        res = []
        helper(nums, [], res)
        return res