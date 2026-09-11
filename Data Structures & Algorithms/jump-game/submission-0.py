class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        possible = [False] * len(nums)

        possible[len(nums) - 1] = True

        for i in range(len(nums)-2, -1, -1):
            
            for jump in range(1, nums[i]+1):
                if possible[i + jump]: 
                    possible[i] = True

                    break

            print(possible[i])
            
        return possible[0]