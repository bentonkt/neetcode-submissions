class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Calculate total product
        total = 1
        non_zero_total = 1

        num_zeroes = 0
        for i, num in enumerate(nums):
            if num == 0:
                num_zeroes += 1
                # If there are 2 or more zeroes, every product will be 0
                if num_zeroes == 2:
                    return [0] * len(nums)
                total *= num
            else:
                non_zero_total *= num
                total *= num


        result = [0] * len(nums)
        for i, num in enumerate(nums):
            if num == 0:
                result[i] = non_zero_total
            else:
                result[i] = int(total / num)
        
        return result