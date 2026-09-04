class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needs = {}

        for i, num in enumerate(nums): 
            if num in needs: 
                return [needs[num], i]

            needs[target - num] = i

        return []