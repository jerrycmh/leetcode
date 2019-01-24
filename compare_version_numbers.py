class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if not version1 and version2:
            return 0
        if not version1:
            return 1
        if not version2:
            return -1
        
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        if len(v1) < len(v2):
            for _ in range(len(v2)-len(v1) ):
                v1.append(0)
        elif len(v2) <  len(v1):
            for _ in range(len(v1) - len(v2)):
                v2.append(0)
        
        for i in range(len(v2)):
            x = int(v1[i]) - int(v2[i])
            if x > 0:
                return 1
            if x < 0:
                return -1
        
        return 0