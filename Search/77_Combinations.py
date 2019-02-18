class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(cur_n, cur_list,res):
            if len(cur_list) == k:
                if cur_list not in res:
                    res.append(cur_list)
                return
            
            for i in range(cur_n, n+1):
                dfs(i+1, cur_list+[i], res)
        
        if not k or not n:
            return []
        res = []
        dfs(1, [], res)
        return res