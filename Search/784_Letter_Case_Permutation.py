class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return [S]
        
        def helper(index, cur_str):
            if index == len(S):
                res.append(cur_str)
                return
            
            if S[index].isalpha():
                helper(index+1, cur_str+S[index].lower())
                helper(index+1, cur_str+S[index].upper())
            else:
                helper(index+1, cur_str+S[index])
        
        
        res = []
        helper(0, "")
        return res