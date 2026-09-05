class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i, num in enumerate(nums):
            # remove this num, and use it for new target 
            dontuse = i

            target = -1 * num

            # Now we do 2sum on sorted list
            l = 0
            r = len(nums) - 1

            while l < r:
                if l == dontuse: 
                    l += 1
                    continue
                if r == dontuse:
                    r -= 1
                    continue
                right = nums[r]
                left = nums[l]

                if right + left == target: 
                    res.add(tuple(sorted([right, left, num])))

                if right + left > target: 
                    r -= 1
                else: 
                    l += 1


        return list(res)
