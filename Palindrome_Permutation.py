class Solution:
    def canPermutePalindrome(self, s: 'str') -> 'bool':
        if not s:
            return True
        
        mapper = {}
        for ch in s:
            if ch not in mapper:
                mapper[ch] = 1
            else:
                mapper[ch] += 1
        
        odd_num = 0
        for key in mapper.keys():
            if mapper[key]%2:
                odd_num += 1
        
        if (odd_num==1 and len(s)%2) or (not odd_num and not len(s)%2):
            return True
        else:
            return False
            