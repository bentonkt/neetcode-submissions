class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        firstDP = [-1] * n
        noFirstDP = [-1] * n

        def dfs(i): 
            if i >= len(nums):
                return 0
            
            if firstDP[i] != -1:
                return firstDP[i]
            
            val = max(dfs(i+1), nums[i] + dfs(i+2))
            firstDP[i] = val
            return val

        def nf(i):
            if i >= len(nums) - 1:
                return 0
            
            if noFirstDP[i] != -1:
                return noFirstDP[i]
            
            val = max(nf(i+1), nums[i] + nf(i+2))
            noFirstDP[i] = val
            return val

        return max(nums[0] + nf(2), dfs(1))
            
        
