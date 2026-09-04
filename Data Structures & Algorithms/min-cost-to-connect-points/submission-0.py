import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        distances = []
        seen = set([0])
        total = 0
        x, y = points[0]
        # get distances for point0
        for i in range(1, len(points)): 
            x2, y2 = points[i]
            distance = abs(x - x2) + abs(y - y2)

            heapq.heappush(distances, (distance, i))

        while len(seen) < len(points): 
            d, p = heapq.heappop(distances)

            if p in seen: 
                continue

            total += d
            seen.add(p)

            x, y = points[p]
            for i in range(len(points)): 
                if i == p: 
                    continue
                x2, y2 = points[i]
                distance = abs(x - x2) + abs(y - y2)

                heapq.heappush(distances, (distance, i))

        return total



                