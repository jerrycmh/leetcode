class Solution:
    def groupStrings(self, strings: 'List[str]') -> 'List[List[str]]':
        if not strings:
            return []
        def decode(s):
            key = str(ord(s[0])-ord(s[0]))+','
            for ch in s[1:]:
                key += str((ord(ch)-ord(s[0]))%26)+','
            return key
        
        diction = {}
        res = []
        
        for string in strings:
            k = decode(string)
            if k not in diction:
                diction[k] = [string]
            else:
                diction[k].append(string)

        for key in diction.keys():
            res.append(diction[key])
        
        return sorted(res)