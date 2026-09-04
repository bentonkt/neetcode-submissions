class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotting = []
        fresh = set()
        # Find all rotting
        for i, x in enumerate(grid): 
            for j, cell in enumerate(x): 
                if cell == 2: 
                    rotting.append((i, j))
                elif cell == 1: 
                    fresh.add((i, j))

        res = 0
        while len(fresh): 
            temp = len(fresh)
            
            for x, y in rotting.copy(): 
                if (x+1, y) in fresh:
                    pos = (x+1, y)
                    fresh.remove(pos)
                    rotting.append(pos)
                if (x, y+1) in fresh: 
                    pos = (x, y+1)
                    fresh.remove(pos)
                    rotting.append(pos)
                if (x, y-1) in fresh:
                    pos = (x, y-1)
                    fresh.remove(pos)
                    rotting.append(pos)
                if (x-1, y) in fresh: 
                    pos = (x-1, y)
                    fresh.remove(pos)
                    rotting.append(pos)

            #No change means that impossible
            if temp == len(fresh): 
                return -1

            res += 1

        return res
            
