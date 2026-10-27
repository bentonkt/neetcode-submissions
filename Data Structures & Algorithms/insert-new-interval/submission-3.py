import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        bisect.insort(intervals, newInterval, key=lambda x: x[0])

        
        merged = []
        for start, end in intervals:
            if not merged:
                merged.append([start, end])
                continue
            
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        return merged