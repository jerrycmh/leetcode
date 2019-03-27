class StockSpanner:

    def __init__(self):
        self.res = []

    def next(self, price: int) -> int:
        cnt = 1
        while self.res and price >= self.res[-1][0]:
            cnt += self.res.pop()[1]
        self.res.append((price, cnt))
        return cnt


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)