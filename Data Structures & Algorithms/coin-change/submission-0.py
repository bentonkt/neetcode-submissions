class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)

        dp[amount] = 0

        for i in range(amount, -1, -1): 
            for coin in coins: 
                if i + coin == amount: 
                    dp[i] = 1
                elif i + coin < amount and dp[i + coin] != -1:
                    ways = 1 + dp[i + coin] 
                    if dp[i] == -1:
                        dp[i] = ways
                    else: 
                        dp[i] = min(ways, dp[i])

        return dp[0]
