class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)

        reverse = defaultdict(list)
        for i in counts:
            reverse[counts[i]].append(i)

        heap = []


        for count in reverse:
            heapq.heappush(heap, -count)


        result = []
        i = k
        while i > 0:
            add = reverse[-heapq.heappop(heap)]
            result.extend(add)
            i-= len(add)

        return result