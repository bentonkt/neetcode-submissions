class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        running = nums[0]
        runningNeg = nums[0]

        for num in nums[1:]: 
            tempRunning = running
            running = max(running * num, num, runningNeg * num)
            runningNeg = min(tempRunning * num, num, runningNeg * num)

            res = max(res, running)

        return res