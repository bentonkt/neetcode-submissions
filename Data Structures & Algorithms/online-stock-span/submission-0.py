class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        temp = []
        count = 1
        while self.stack and price >= self.stack[-1]:
            temp.append(self.stack.pop())
            count += 1

        

        while temp: 
            self.stack.append(temp.pop())
        self.stack.append(price)

        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)