class StockSpanner:
    def __init__(self):
        self.history = []

    def next(self, price: int) -> int:
        count = 1
        while self.history and price >= self.history[-1][0]:
            ndays = self.history.pop()[1]
            count += ndays
        self.history.append((price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
prices = [7,2,1,2]
for price in prices:
    print(obj.next(price))
