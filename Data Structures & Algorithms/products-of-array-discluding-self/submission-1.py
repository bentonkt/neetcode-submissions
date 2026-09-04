class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Compute prefixes
        result = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                result[i] = 1
            else:
                result[i] = result[i-1] * nums[i-1]
        print(result)
        # Compute postfixes
        postfixes = [0] * len(nums)
        i = len(nums) - 1 
        while i >= 0:
            if i == len(nums) - 1:
                postfixes[i] = 1
            else:
                postfixes[i] = nums[i+1] * postfixes[i + 1]
            i -= 1

        i = len(nums) - 1 
        while i >= 0:
            if i == len(nums) - 1:
                i-=1
                continue
            else:
                result[i] = result[i] * postfixes[i]
            i -= 1

        return result