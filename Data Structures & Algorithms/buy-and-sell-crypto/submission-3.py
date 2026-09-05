class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum = float('inf')
        res = 0
        for i, price in enumerate(prices):

            if price - minimum > res:
                res = price - minimum

            if price < minimum: 
                minimum = price

        return res