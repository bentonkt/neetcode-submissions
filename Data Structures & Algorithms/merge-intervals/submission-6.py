import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)

        start, end = heapq.heappop(intervals)
        cur_min = start
        cur_max = end
        cur = [start, end]
        res = []

        while intervals: 
            start, end = heapq.heappop(intervals)
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