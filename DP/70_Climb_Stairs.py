class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        
        num_seq = [1, 2]
        for i in range(1, n-1):
            num_seq.append(num_seq[i]+num_seq[i-1])
        return num_seq[-1]