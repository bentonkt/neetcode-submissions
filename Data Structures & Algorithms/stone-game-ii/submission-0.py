class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dp[i, M] = maximum number of stones first player can get from piles[i:] with M

        dp = {}

        prefixSums = [0]
        for i, pile in enumerate(piles): 
            prefixSums.append(prefixSums[i] + piles[i])

        total = sum(piles)

        def dfs(i, M): 
            if i >= len(piles): 
                return 0


            if (i, M) in dp: 
                return dp[(i, M)]

            # decide how many stones to take, up to 2M
            val = 0
            remaining = total - prefixSums[i]
            for j in range(1, 2*M+1): 
                val = max(val, remaining - dfs(i+j, max(M, j)))

            dp[(i, M)] = val
            return val
                

        result = dfs(0, 1)
        return result
