class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = set()

        for i, num in enumerate(nums): 
            target = -num

            l, r = i+1, len(nums) - 1

            while l < r: 
                val = nums[l] + nums[r]
                if val == target: 
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -=1
                elif val > target: 
                    r -= 1
                else: 
                    l += 1

        return list(res)