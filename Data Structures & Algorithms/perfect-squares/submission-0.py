class Solution:
    def numSquares(self, n: int) -> int:
        
        limit = math.ceil(math.sqrt(n))


        dp = [-1] * (n+1)

        def dfs(i):
            if dp[i] != -1: 
                return dp[i]

            limit = math.floor(math.sqrt(i))

            if limit ** 2 == i: 
                dp[i] = 1
                return 1

            least = float('inf')
            for j in range(limit, 0, -1):
                val = dfs(i-j**2)
                least = min(val, least)

            dp[i] = 1+least
            return 1+least



        return dfs(n)

