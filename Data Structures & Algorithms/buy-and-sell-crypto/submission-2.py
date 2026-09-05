class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum = float('inf')
        res = 0
        for i, price in enumerate(prices):

            
            res = max(res, price - minimum)

            minimum = min(price, minimum)

        return res