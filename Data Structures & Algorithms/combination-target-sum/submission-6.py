class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()

        def dfs(i, a): 
            if i >= len(nums):
                return

            nonlocal res


            num = nums[i]

            soFar = sum(a)
            # if memo[(soFar, i)]:
            #     return
            if soFar > target: 
                return

            if soFar + num == target:
                a.append(num)
                res.add(tuple(a))
                a.pop()

            dfs(i+1, a.copy())

            if soFar + num > target:
                return

            a.append(num)
            dfs(i, a.copy())
            

        dfs(0, [])

        return [list(c) for c in res]
