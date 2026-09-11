class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = [-1] * len(nums)

        jumps[len(nums)-1] = 0

        for i in range(len(nums)-2, -1, -1): 
            l = nums[i]
            minimum = float('inf')
            for j in range(1, min(len(nums) - i, l+1)): 
                if jumps[i + j] > -1: 
                    minimum = min(minimum, jumps[i +j] +1)

            jumps[i] = minimum
            # print(minimum)

        return jumps[0]