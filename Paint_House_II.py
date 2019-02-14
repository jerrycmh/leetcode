class Solution:
    def minCostII(self, costs: 'List[List[int]]') -> 'int':
        if not costs:
            return 0
        if len(costs) == 1:
            return min(costs[0])
        if len(costs) > 1 and len(costs[0]) == 1:
            return 0
        
        res = [costs[0]]
        for i in range(1, len(costs)):
            temp = []
            for j in range(len(costs[i])):
                min_cost = float('inf')
                for k in range(len(res[-1])):
                    if j != k: min_cost = min(min_cost, res[-1][k]+costs[i][j])
                temp.append(min_cost)
            res.append(temp)
        
        return min(res[-1])