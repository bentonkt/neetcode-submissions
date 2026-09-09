class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [[(x1 ** 2 + x2 ** 2) ** (1/2), x1, x2] for x1, x2 in points]

        heapq.heapify(dists)
        res = []
        for i in range(k):
            d = heapq.heappop(dists)

            res.append(d[1:])


        return res