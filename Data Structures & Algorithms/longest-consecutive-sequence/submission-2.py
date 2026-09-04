class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # True is top
        # False is bottom

        check = set(nums)

        res = 0
        for num in nums: 
            if num-1 not in check: 
                running = 1
                while num+1 in check: 
                    running += 1
                    num += 1

                res = max(res, running)

        return res