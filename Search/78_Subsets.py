class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(num_set, cur_set, res):
            if cur_set not in res:
                res.append(cur_set)
            if len(cur_set) == len(nums):
                return
            for i, num in enumerate(num_set):
                    dfs(num_set[i+1:], cur_set+[num], res)
        
        result = []
        dfs(nums, [], result)
        return result