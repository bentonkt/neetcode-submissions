class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0


        prefixSums = defaultdict(int)
        prefixSums[0] += 1
        prefix = 0
        for i, num in enumerate(nums): 
            prefix += num
            # print(prefix)
            # print(prefixSums)

            
            # print("minus" + str(prefix-k))
            res += prefixSums[prefix-k]
            prefixSums[prefix] += 1
            # print(res)

           

        # print(prefixSums)


        return res



