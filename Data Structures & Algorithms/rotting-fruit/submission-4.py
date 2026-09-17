class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh = set()
        for i, row in enumerate(grid): 
            for j, num in enumerate(row):
                if num == 2:
                    rotten.append([i, j])
                if num == 1:
                    fresh.add((i, j))

        if not rotten:
            if fresh:
                return -1
            else: 
                return 0

        # Do BFS from each node every time
        minutes = 0
        
        while rotten:
            if len(fresh) == 0:
                return minutes

            copy = rotten.copy()
            rotten = []
            for y, x in copy: 
                # BFS from this node

                if (y+1, x) in fresh:
                    fresh.remove((y+1, x))
                    rotten.append([y+1, x])
                if (y, x+1) in fresh:
                    fresh.remove((y, x+1))
                    rotten.append([y, x+1])
                if (y-1, x) in fresh:
                    fresh.remove((y-1, x))
                    rotten.append([y-1, x])
                if (y, x-1) in fresh:
                    fresh.remove((y, x-1))
                    rotten.append([y, x-1])

            minutes += 1
            
        if len(fresh) == 0:
                return minutes
        return -1