class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = deque([])
        

        counts = Counter(tasks)
        print(counts)

        heap = [-c for c in counts.values()]
        heapq.heapify(heap)

        time = 0

        while heap or cooldown: 
            # check cooldowns
            while cooldown: 
                t, c = cooldown[0]
                if t != time: 
                    break
                cooldown.popleft()
                heapq.heappush(heap, c)

            # Cooldowns are caught up
            if heap:
                count = heapq.heappop(heap)
                count += 1
                if count != 0: 
                    cooldown.append((time + n+1, count))

            time += 1

        return time