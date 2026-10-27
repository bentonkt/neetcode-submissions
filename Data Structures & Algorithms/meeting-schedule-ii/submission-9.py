"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        changes = defaultdict(int)
        for interval in intervals:
            start, end = interval.start, interval.end
            changes[start]+=1
            changes[end]-=1

        rooms = 0
        running = 0
        for num in sorted(changes.keys()):
            running += changes[num]
            rooms = max(rooms, running)

        return rooms