class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[i, total] = # of ways to get from amount to target with nums[i:]

        dp = {}

        def dfs(i, total): 
            if i == len(nums): 
                if total == target: 
                    return 1
                else:
                    return 0

            if (i, total) in dp: 
                return dp[(i, total)]

            # add this one
            res1 = dfs(i+1, total + nums[i])

            # subtract this one
            res2 = dfs(i+1, total - nums[i])

            dp[(i, total)] = res1 + res2

            return res1 + res2


        return dfs(0, 0)