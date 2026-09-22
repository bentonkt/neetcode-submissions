class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = set()

        def dfs(num, arr, i):
            nonlocal res
            

            if num == 0: 
                res.add(tuple(arr))
                return 
            
            if i > n: 
                return
            

            # add this one

            arr.append(i)
            dfs(num-1, arr, i+1)

            # dont add this one
            arr.pop()
            dfs(num, arr, i+1)
            
            return

        dfs(k, [], 1)
        return [list(elem) for elem in res]



