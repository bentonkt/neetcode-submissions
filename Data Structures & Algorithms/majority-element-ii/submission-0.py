class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) / 3

        counts = defaultdict(int)
        res = set()

        for num in nums:
            counts[num] += 1
            
            if counts[num] > threshold:      
                res.add(num)


        return list(res)