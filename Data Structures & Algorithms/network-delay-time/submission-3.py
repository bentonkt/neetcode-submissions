class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # mst
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, u, v))

        queue = []
        heapq.heapify(queue)

        for item in adj[k]:
            heapq.heappush(queue, item)
        
        
        visited = set([k])
        total = 0

        costs = {k:0}

        while queue:

            t, u, v = heapq.heappop(queue)
            if v in visited:
                continue
            visited.add(v)
            costs[v] = t

            if len(visited) == n:
                return max(costs.values())

            # we hit node v
            for t1, u1, v1 in adj[v]:
                heapq.heappush(queue, (costs[u1] + t1, u1, v1))

        # Could connect all nodes
        return -1
        
