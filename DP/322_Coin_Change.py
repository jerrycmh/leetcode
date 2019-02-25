class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float('inf') for _ in range(amount)]
        
        for i in range(1, amount+1):
            temp = []
            for c in coins:
                if i-c >=0: temp.append(dp[i-c])
                if temp: dp[i] = min(temp)+1
        
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]