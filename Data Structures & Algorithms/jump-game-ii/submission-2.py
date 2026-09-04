class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo = {}

        for i in range(len(nums) - 1, -1, -1):
            print(i)
            num = nums[i]
            if i == len(nums) - 1:
                memo[i] = 0
            elif i + num >= len(nums) - 1:
                memo[i] = 1
            else: 
                minimum = float('inf')
                for j in range(1, num+1):
                    index = i + j
                    minimum = min(minimum, memo[index])

                memo[i] = 1 + minimum
        print(memo)
        return memo[0]
