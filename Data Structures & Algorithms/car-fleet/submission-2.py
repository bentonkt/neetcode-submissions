import heapq

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []

        heap = []
        n = len(position)
        for i in range(n): 
            p, s = position[i], speed[i]

            heapq.heappush(heap, (p,s))


        # O(nlogn)
        def willCatch(p1, s1, p2, s2):
            diff = s1-s2
            if diff <= 0: 
                return False

            time = (p2-p1) / diff
            end = (target-p2) / s2
            # print(time)
            # print(end)
            if time <= end:
                return True

            return False


        while heap: 
            # print(heap)
            # print(fleet)
            # print("___")
            p, s = heapq.heappop(heap)

            while fleet and willCatch(fleet[-1][0], fleet[-1][1], p, s): 
                fleet.pop()

            fleet.append((p, s))

        return len(fleet)  

            