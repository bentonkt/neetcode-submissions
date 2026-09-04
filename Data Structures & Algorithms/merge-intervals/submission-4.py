import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pq = []

        for interval in intervals:
            heapq.heappush(pq, (interval[0], interval[1]))

        start, end = heapq.heappop(pq)

        cur_min = start
        cur_max = end
        cur = [start, end]
        res = []

        while pq: 
            start, end = heapq.heappop(pq)
            # Max interval if overlap
            if start <= cur_max: 
                cur_max = max(cur_max, end)
            else: 
                # no overlap
                res.append([cur_min, cur_max])
                cur_min = start
                cur_max = end

        res.append([cur_min, cur_max])

        return res