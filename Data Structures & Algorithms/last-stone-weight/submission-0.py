import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) >= 2:
            stone1 = heapq.heappop(heap)

            stone2 = heapq.heappop(heap)

            res = -abs(stone1-stone2)
            heapq.heappush(heap, res)

        return -1 * heap[0]