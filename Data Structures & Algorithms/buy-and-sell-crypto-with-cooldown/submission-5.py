class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, holding): 
            if i >= len(prices): 
                return 0

            if (i, holding) in dp: 
                return dp[(i, holding)]

            if holding: 
                # decide to sell
                res1 = prices[i] + dfs(i+2, False )

                # hold
                res2 = dfs(i+1,True)

                dp[(i, holding)] = max(res1, res2)

                return dp[(i, holding)]

            else: 
                # buy
                res1 = dfs(i+1, True) - prices[i]

                # dont buy
                res2 = dfs(i+1, False)

                dp[(i, holding)] = max(res1, res2)

                return dp[(i, holding)]


        return dfs(0, False)


