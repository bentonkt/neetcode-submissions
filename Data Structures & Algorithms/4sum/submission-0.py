class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = set()
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)):
                num1, num2 = nums[i], nums[j]
                subTarget = target - num1 - num2

                l, r = j+1, len(nums) - 1

                while l < r: 
                    val = nums[l] + nums[r]
                    if val == subTarget: 
                        res.add((num1, num2, nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif val < subTarget: 
                        l += 1
                    else: 
                        r -= 1

        return [list(x) for x in res]