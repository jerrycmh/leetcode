class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        if n == 0:
            return []
        
        def backtrack(cur_string, left, right):
            if len(cur_string) == 2*n:
                res.append(cur_string)
                return
            if left < n:
                backtrack(cur_string+"(", left+1, right)
            if right < left:
                backtrack(cur_string+")", left, right+1)
        
        res = []
        backtrack("", 0, 0)
        return res