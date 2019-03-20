class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or haystack == needle:
            return 0
        
        res = -1
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                res = i
                for j in range(len(needle)):
                    if haystack[i+j] != needle[j]:
                        res = -1
                        break
                if res != -1:
                    return res
        return res