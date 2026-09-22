class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        adj = defaultdict(list)

        for i in range(len(equations)): 
            u, v = equations[i]
            value = values[i]

            adj[u].append((v, value))
            adj[v].append((u, 1 / value))


        res = []

        for u, v in queries: 


            # dfs from u to v
            visited = set()

            def dfs(node, acc): 
                if node not in adj:
                    return -1.0

                if node == v: 
                    return acc

                if node in visited: 
                    return -1.0

                visited.add(node)

                

                neighbors = adj[node]

                for neighbor, value in neighbors:
                    val = dfs(neighbor, acc * value)
                    if val != -1.0: 
                        return val
                return -1.0

            res.append(dfs(u, 1))
            

        return res
