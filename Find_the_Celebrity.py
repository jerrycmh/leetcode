# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(1, n):
            if knows(res, i):
                res = i
        
        for i in range(n):
            if i != res:
                if not knows(res, i) and knows(i, res):
                    continue
                else:
                    return -1
        
        return res