class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSums = [0]

        for i, num in enumerate(nums): 

            prefixSums.append(num + prefixSums[i])

        res= 0
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                val = prefixSums[j+1] - prefixSums[i]
                if val % k == 0:
                    res += 1

        return res
