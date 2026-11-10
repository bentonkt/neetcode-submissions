class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # aaxxyxy
        # c, i: # of ways to form t[i:]
        indices = defaultdict(list)
        for i, c in enumerate(s):
            indices[c].append(i)

        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1

            if j > len(t)-1 or i > len(s) - 1: 
                return 0

            if (i, j) in dp: 
                return dp[(i, j)]

            c = t[j]
            choices = indices[c]

            res = 0

            for index in choices: 
                if index < i: 
                    continue

                res += dfs(index+1, j+1)

            dp[(i, j)] = res
            return res
                

        res = dfs(0, 0)
        print(dp)
        return res


            