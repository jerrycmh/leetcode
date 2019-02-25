class Solution:
    def numTilings(self, N: int) -> int:
        if N == 0 or N == 1:
            return 1
        if N == 2:
            return 2
        if N == 3:
            return 5
        
        dp = [0 for _ in range(N)]
        dp[0] = 1
        dp[1] = 2
        dp[2] = 5
        
        for i in range(3, N):
            dp[i] = (2*dp[i-1]+dp[i-3]) % (10**9+7)
        
        print(dp)
        return dp[-1]