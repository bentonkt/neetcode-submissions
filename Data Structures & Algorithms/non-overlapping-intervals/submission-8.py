class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])
        res = 0
        prev = None
        for start, end in intervals:
            if prev and start < prev:
                res += 1
            else:
                prev = end

        return res
            