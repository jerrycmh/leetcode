class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        graph = {}
        for num in nums:
            if num not in graph:
                graph[num] = 1
            else:
                graph[num] += 1
        dp_size = max(nums)
        dp = [0 for _ in range(dp_size+1)]
        if 1 in nums:
            dp[1] = graph[1]
        else:
            dp[1] = 0
            
        for i in range(2, dp_size+1):
            if i in nums:
                dp[i] = max(dp[i-1], i*graph[i]+dp[i-2])
            else:
                dp[i] = dp[i-1]

        return dp[-1]