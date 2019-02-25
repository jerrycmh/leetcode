class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for i in prices:
            if i < min_price:
                min_price = i
            elif i-min_price > max_profit:
                max_profit = i-min_price
            else:
                pass
        return max_profit