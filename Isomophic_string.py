class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}
        
        for i in range(len(s)):
            if s[i] not in s_map and t[i] not in t_map:
                s_map[s[i]] = i
                t_map[t[i]] = i
            elif s[i] in s_map and t[i] in t_map:
                if s_map[s[i]] != t_map[t[i]]:
                    return False
            else:
                return False
        
        return True