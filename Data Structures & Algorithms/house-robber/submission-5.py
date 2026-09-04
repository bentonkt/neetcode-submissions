class Solution:
    def helper(self, nums, index): 
        if index >= len(nums): 
            return 0
        if index in self.values: 
            return self.values[index]
        else: 
            arr = nums[index:]
            if len(arr) == 0: 
                return 0
            elif len(arr) == 1: 
                return arr[0]
            elif len(arr) == 2:
                return max(arr)
            elif len(arr) == 3: 
                return max(arr[0] + arr[2], + arr[1])

             # Choose first 
            first = nums[index] + self.helper(nums, index+2)

            # Choose second
            second = nums[index+1] + self.helper(nums, index+3)

            res = max(first, second)
            self.values[index] = res
            return res



    def rob(self, nums: List[int]) -> int:
        self.values = {}

        return self.helper(nums, 0)