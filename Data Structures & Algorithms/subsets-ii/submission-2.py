class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        def backtrack(i, arr):

            if i >= len(nums): 
                res.add(tuple(arr))
                return

            # Add this one
            arr.append(nums[i])
            backtrack(i+1, arr)

            # dont add this one
            arr.pop()
            backtrack(i+1, arr)


        backtrack(0, [])

        return [list(elem) for elem in res]