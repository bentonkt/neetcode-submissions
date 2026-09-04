class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = defaultdict(lambda: -1)

        for i, num in enumerate(nums):
            print(values)
            if values[num] != -1:
                return [min(i, values[num]), max(i, values[num])]

            else:
                key = target - num
                values[key] = i
        return [0,0]