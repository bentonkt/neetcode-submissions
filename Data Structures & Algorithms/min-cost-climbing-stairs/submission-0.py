class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 2:
            return min(cost[:2])

        dp = [0] * (n+1)
        dp[n] = 0
        dp[n-1] = cost[n-1]
        dp[n-2] = cost[n-2]

        for i in range(n-3, -1, -1): 
            base = cost[i]
            if dp[i+1] < dp[i+2]:
                base += dp[i+1]
            else: 
                base += dp[i+2]

            dp[i] = base

        return min(dp[:2])
