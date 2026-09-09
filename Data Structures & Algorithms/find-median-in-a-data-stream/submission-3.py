class MedianFinder:

    def __init__(self):
        self.length = 0
        self.prefix = [] # max heap
        self.suffix = [] # min heap

    def addNum(self, num: int) -> None:
        self.length += 1

        if self.prefix and num <= -self.prefix[0]:
            heapq.heappush(self.prefix, -num)
        else: 
            heapq.heappush(self.suffix, num)

        while len(self.prefix) - len(self.suffix) > 1:
            heapq.heappush(self.suffix, -1 * heapq.heappop(self.prefix))
        while len(self.suffix) - len(self.prefix) > 1:
            heapq.heappush(self.prefix, -1 * heapq.heappop(self.suffix))


        

        

    def findMedian(self) -> float:
        if self.length % 2:
            median = self.suffix[0] if len(self.suffix) > len(self.prefix) else -self.prefix[0]
        else:
            median = (-self.prefix[0] + self.suffix[0]) / 2

        return median