class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeros = 0
        index = -1
        for i, num in enumerate(nums): 
            if num == 0: 

                if numZeros:
                    return [0] * len(nums)

                numZeros += 1
                index = i
        
        if numZeros:
            res = [0] * len(nums)
            total = 1
            for i in range(0, index):
                total *= nums[i]
            for i in range(index+1, len(nums)): 
                total *= nums[i]
            res[index] = total
            return res
        
        prefix = 1
        suffix = 1
        for num in nums[1:]: 
            suffix *= num
        res = [1] * len(nums)
        res[0] = suffix
        for i in range(1, len(nums)):
            num = nums[i]
            prefix *= nums[i-1]
            suffix /= num

            res[i] = int(prefix * suffix)

        return res