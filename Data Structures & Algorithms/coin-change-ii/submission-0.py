class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i, total] = # ways to get from total to target, using coins[i:]
        dp = {}
        def dfs(i, total): 
            if total > amount or i >= len(coins): 
                return 0
            if total == amount: 
                return 1
            
            if (i, total) in dp: 
                return dp[(i, total)]


            # Use this coins
            res1 = dfs(i, total+coins[i])
            # dont use this coins
            res2 = dfs(i+1, total)

            dp[(i, total)] = res1 + res2
            return res1 + res2

        return dfs(0, 0)
