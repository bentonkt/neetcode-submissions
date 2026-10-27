class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        n = len(intervals)
        res = []
        cur = intervals[0]
        for i, interval in enumerate(intervals):
            start, end = interval

            if start <= cur[1]:
                cur[1] = max(cur[1], end)
            else:
                res.append(cur)
                cur = [start, end]
            if i == n-1:
                res.append(cur)

        return res

            