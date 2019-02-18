class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def dfs(cur_list, res):
            if sum(cur_list) == target:
                if sorted(cur_list) not in res:
                    res.append(cur_list)
                return
            for num in candidates:
                if num+sum(cur_list) <= target:
                    dfs(cur_list+[num], res)
            return
        
        if not candidates:
            return []
        candidates = sorted(candidates)
        res = []
        dfs([], res)
        return res