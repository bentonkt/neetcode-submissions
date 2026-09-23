class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp[i, j] is how much the first player wins/loses by on piles[i:j]

        dp = {}

        def dfs(i, j): 
            if i == j: 
                dp[(i, j)] = piles[i]
                return piles[i]

            if (i, j) in dp: 
                return dp[(i, j)]

            # Take from left:
            res1 = piles[i] - dfs(i+1, j)

            # Take from rgith: 
            res2 = piles[j] - dfs(i,j -1)

            
            best = max(res1, res2)

            dp[(i, j)] = best

            return best


        return dfs(0, len(piles)-1) > 0