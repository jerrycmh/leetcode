class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k > 9:
            return []
        def dfs(num, cur_list, res):

            if len(cur_list) == k:
                if sum(cur_list) == n:
                    res.append(cur_list)
                return
            if num > 9:
                return
            
            for i in xrange(num, 10):
                if i+sum(cur_list) <= n:
                    dfs(i+1, cur_list+[i], res)
        
        result = []
        dfs(1, [], result)
        return result