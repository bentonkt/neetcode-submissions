class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minimum = float('inf')

        prefixSums = [0]

        for i, num in enumerate(nums): 
            prefixSums.append(prefixSums[i] + num)

        l = 0

        for i in range(1, len(nums)+1): 
            while prefixSums[i] - prefixSums[l] >= target:
                minimum = min(minimum, i-l)
                l += 1

        if minimum == float('inf'):
            return 0
        else: 
            return minimum

