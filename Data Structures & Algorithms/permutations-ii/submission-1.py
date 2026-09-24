class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        used = set()
        path = []

        def dfs(): 
            if len(path) == len(nums): 
                res.add(tuple(path))
                return

            for i, num in enumerate(nums): 
                if i in used: 
                    continue

                path.append(num)
                used.add(i)

                dfs()

                path.pop()
                used.remove(i)

        dfs()

        return [list(elem) for elem in res]