"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        numbers = defaultdict(int)

        for interval in intervals:
            numbers[interval.start] += 1
            numbers[interval.end] -= 1


        res = 0
        running = 0
        for num in sorted(numbers.keys()):
            running += numbers[num]
            res = max(running, res)

        return res