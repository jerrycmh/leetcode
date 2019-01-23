class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False
        if abs(len(s) - len(t)) > 1:
            return False
        if not s or not t:
            return True
        
        size = max(len(s), len(t))
        i, j = 0, 0
        find_diff = False
        
        while i < len(s) and j < len(t):
            print i, j
            if s[i] != t[j]:
                if i == size-1 and j == size-1:
                    return not find_diff
                if find_diff:
                    return False
                else:
                    # Try Diff
                    if len(s) < len(t) and s[i] == t[j+1]:
                        j += 1
                    elif len(s) > len(t) and s[i+1] == t[j]:
                        i += 1
                    elif len(s) == len(t) and s[i+1] == t[j+1]:
                        i += 1
                        j += 1
                    else:
                        return False
                    find_diff = True
            else:
                i += 1
                j += 1
        
        if i != len(s) or j != len(t):
            return not find_diff
        
        return find_diff