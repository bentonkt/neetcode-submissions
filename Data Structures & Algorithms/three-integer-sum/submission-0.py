class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i, num in enumerate(nums):
            # remove this num, and use it for new target 
            nums.pop(i)

            target = -1 * num

            # Now we do 2sum on sorted list

            l = 0
            r = len(nums) - 1

            while l < r:
                right = nums[r]
                left = nums[l]

                if right + left == target: 
                    res.add(tuple(sorted([right, left, num])))

                if right + left > target: 
                    r -= 1
                else: 
                    l += 1

            nums.insert(i, num)

        return list(res)
