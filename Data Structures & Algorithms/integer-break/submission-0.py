class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        if n == 2:
            return 1
        dp[2] = 1
        dp[3] = 2

        for i in range(4, n+1): 
            for j in range(0, i): 
                best = max(j, dp[j]) * max(i-j, dp[i-j])
                dp[i] = max(best, dp[i])
        
        return dp[n]
