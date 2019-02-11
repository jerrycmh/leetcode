class Solution:
    def isStrobogrammatic(self, num: 'str') -> 'bool':
        if not num:
            return True
        
        front, end = "", ""
        size = len(num)
        if size%2:
            if num[size//2] not in ['0','1','8','0']:
                return False
            front = num[:(size//2)]
            end = num[(size//2+1):]
        else:
            front = num[:(size//2)]
            end = num[(size//2):]
        
        i = 0
        s = size//2
        while i != s:
            
            if front[i] != end[s-i-1]:
                if (front[i] == "6" and end[s-i-1] == "9") or (front[i] == "9" and end[s-i-1] == "6"):
                    pass
                else:
                    return False
            else:
                if front[i] not in ['0','1','8','0'] or end[s-i-1] not in ['0','1','8','0']:
                    return False
            i += 1
        return True