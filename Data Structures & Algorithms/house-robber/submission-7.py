class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def dfs(i): 
            if i >= len(nums):
                return 0
            if memo[i] != -1: 
                return memo[i]

            # hasn't been done before
            # take it or you go to the next one
            value = max(dfs(i+1), nums[i] + dfs(i+2))
            memo[i] = value
            return value

        return dfs(0)