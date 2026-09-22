class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, p in flights: 
            adj[u].append((v, p))

        queue = [(0, src, 0)]
        visited = {}

        while queue: 
            p, u, steps = heapq.heappop(queue)


            if steps > k+1: 
                continue
            if u == dst: 
                return p
            if u in visited and steps >= visited[u]: 
                continue

            visited[u] = steps


            neighbors = adj[u]
            for v, cost in neighbors: 
                heapq.heappush(queue, (p+cost, v, steps+1))

            
        return -1
