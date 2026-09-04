class Solution:
    def helper(self, arr, nums):
        if len(nums) == 0: 
            self.res.append(arr)

        else: 

            self.helper(arr + [nums[0]], nums[1:])
            self.helper(arr, nums[1:])



    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.res = []
        self.helper([], nums)
        
        return self.res

        