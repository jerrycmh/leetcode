class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left_rem, right_rem = 0, 0
        for c in s:
            if c == "(":
                left_rem += 1
            elif c == ")":
                if left_rem == 0:
                    right_rem += 1
                else:
                    left_rem -= 1
        
        res = []
        
        def dfs(depth, left, right, left_p, right_p, cur_str):
            if depth == len(s):
                if left == 0 and right == 0 and cur_str not in res:
                    res.append(cur_str)
            else:
                if s[depth] == "(" and left > 0:
                    dfs(depth+1, left-1, right, left_p, right_p, cur_str)
                if s[depth] == ")" and right > 0:
                    dfs(depth+1, left, right-1, left_p, right_p, cur_str)
                if s[depth] != "(" and s[depth] != ")":
                    dfs(depth+1, left, right, left_p, right_p, cur_str+s[depth])
                elif s[depth] == "(":
                    dfs(depth+1, left, right, left_p+1, right_p, cur_str+"(")
                elif s[depth] == ")" and left_p > right_p:
                    dfs(depth+1, left, right, left_p, right_p+1, cur_str+")")
        
        dfs(0, left_rem, right_rem, 0, 0, "")
        return res