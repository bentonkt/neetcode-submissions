class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        l, r = 0, 0
        total = 1
        res = 0

        while r < len(nums):
            total *= nums[r]
            if total < k:
                # every subarray between l and r is < k
                # just count the ones starting from l 
                # l, l+1, ..., l+k
                res += r - l + 1
            else: 
                while total >= k and l< r:
                    total //= nums[l]
                    l += 1

                # total < k 
                if total < k: 
                    res += r - l + 1

            r += 1

        return res
            
