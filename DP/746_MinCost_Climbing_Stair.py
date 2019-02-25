class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost: 
            return 0
        if len(cost) == 1:
            return cost[0]
        
        result = [0 for _ in range(len(cost)+1)]
        
        for i in range(2, len(result)):
            result[i] = min(cost[i-1]+result[i-1], result[i-2]+cost[i-2])

        return result[-1]