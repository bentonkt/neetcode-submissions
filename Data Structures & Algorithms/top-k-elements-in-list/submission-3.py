class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)

        n = []
        for c in count:
            heapq.heappush(n, (-count[c], c))

        # Pop k elements from the heap
        res = []
        for i in range(k):
            res.append(heapq.heappop(n)[1])
                
        return res
