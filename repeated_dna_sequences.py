class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        
        appeared = {}
        result = []
        for i in range(len(s)-9):
            temp = s[i:i+10]
            if temp not in appeared:
                appeared[temp] = 1
            else:
                appeared[temp] += 1
        
        for key in appeared:
            if appeared[key] > 1:
                if key not in result:
                    result.append(key)
        return result