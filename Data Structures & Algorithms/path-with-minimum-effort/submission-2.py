class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0,0,0)]

        visited = set()

        nexts = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        while heap: 
            e, i, j = heapq.heappop(heap)

            if i == len(heights)-1 and j == len(heights[0])-1:
                return e

            if (i, j) in visited:
                continue

            visited.add((i, j))

            # neighbors
            for y, x in nexts: 
                if 0 <= y+i and y+i < len(heights) and 0 <= x+j and x+j < len(heights[0]):
                    height = heights[y+i][x+j]
                else:
                    continue

                diff = abs(heights[i][j] - height)

                f = max(e, diff)

                heapq.heappush(heap, (f, y+i, x+j))

        return -1

