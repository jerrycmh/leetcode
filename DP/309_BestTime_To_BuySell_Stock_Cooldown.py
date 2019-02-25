class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        size = len(prices)
        
        #Cool down state s0
        s0 = [0 for _ in range(size+1)]
        #Buy in state s1
        s1 = [-prices[0] for _ in range(size+1)]
        #Sell out state s2
        s2 = [-1 for _ in range(size+1)]
        
        for i in range(1, size+1):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s0[i-1]-prices[i-1], s1[i-1])
            s2[i] = s1[i-1]+prices[i-1]
        
        return max(s2[-1], s0[-1])