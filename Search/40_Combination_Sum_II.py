class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def dfs(candi,cur_list,res):
            if sum(cur_list) == target:
                if sorted(cur_list) not in res:
                    res.append(cur_list)
                    return
            
            if not candi:
                return
            
            for i in xrange(len(candi)):
                num = candi[i]
                if sum(cur_list)+num <= target:
                    dfs(candi[i+1:],cur_list+[num],res)
            
        if not candidates:
            return []
        res = []
        candidates = sorted(candidates)
        dfs(candidates, [], res)
        
        return res