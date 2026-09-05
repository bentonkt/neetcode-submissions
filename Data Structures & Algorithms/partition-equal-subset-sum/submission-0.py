class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: 
            return False

        target = sum(nums) / 2
        subset = []
        def dfs(i, goal):
            if goal == 0: 
                return True

            if goal < 0 or i >= len(nums)-1: 
                return False

            num = nums[i]

            if dfs(i+1, goal - num):
                return True
            if dfs(i+1, goal):
                return True

            return False

        return dfs(0, target)

        

            
