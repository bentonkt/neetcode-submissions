class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        running = 0

        for i in range(len(nums)): 
            running += nums[i]
            res = max(res, running)

            if running < 0: 
                running = 0

        return res

