class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        total = 0

        prev = prices[0]
        for i, price in enumerate(prices[1:]):
            if prev < price: 
                total += price - prev

            prev = price

        return total

