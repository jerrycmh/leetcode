class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        res = ""
        for c in s.lower():
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                res += c
            elif c >= '0' and c <= '9':
                res += c

        i, j = 0, len(res)-1
        while i<=j :
            if res[i] != res[j]:
                return False
            i += 1
            j -= 1
        return True