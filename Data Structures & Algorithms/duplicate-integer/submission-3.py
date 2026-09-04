class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stuff = set()
        for num in nums: 
            if num in stuff: 
                return True

            else: 
                stuff.add(num)

        return False