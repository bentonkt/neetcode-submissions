class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        path = []

        res = []

        remaining = [n, n]

        def dfs(): 
            if remaining == [0,0]:
                res.append("".join(path))

            if remaining[0] == remaining[1]:
                path.append("(")
                remaining[0] -= 1
                dfs()
                path.pop()
                remaining[0] += 1

            else:
                if remaining[0] > 0:
                    path.append("(")
                    remaining[0] -= 1
                    dfs()
                    path.pop()
                    remaining[0] += 1

                if remaining[1] >0:
                    path.append(")")
                    remaining[1] -= 1
                    dfs()
                    path.pop()
                    remaining[1] += 1

        dfs()
        return res
