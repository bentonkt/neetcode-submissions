class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(num, arr, i):
            nonlocal res
            

            if num == 0: 
                res.append(arr.copy())
                return 
            
            if i > n: 
                return
            

            # add this one
            new = arr.copy()
            new.append(i)
            dfs(num-1, new, i+1)

            # dont add this one
            dfs(num, arr, i+1)
            
            return

        dfs(k, [], 1)
        return res



