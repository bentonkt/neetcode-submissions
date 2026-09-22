class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, arr):

            if i >= len(nums): 
                res.append(tuple(arr))
                return

            # Add this one
            arr.append(nums[i])
            backtrack(i+1, arr)

            # dont add this one
            arr.pop()
            val = nums[i]
            while i < len(nums) and nums[i] == val:
                i+=1
            backtrack(i, arr)


        backtrack(0, [])
        return res
        return [list(elem) for elem in res]