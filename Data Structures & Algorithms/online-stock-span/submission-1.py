class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        index = len(self.stack) - 1

        while index >= 0 and self.stack[index] <= price:
            index -= 1
            count += 1

        self.stack.append(price)

        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)