class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = []
        for i, x in enumerate(gas): 
            diffs.append(x - cost[i])

        a = 0
        index = None
        for i, diff in enumerate(diffs): 
            a += diff

            if a < 0: 
                index = None
                a = 0
                continue
            # Start a running sum from this index if we don't have one already
            if index == None: 
                index = i


        if index == None: 
            return -1
        else: # We ahve a runner
            i = 0
            while i < index: 
                a += diffs[i]
                if a < 0: 
                    return -1
                i += 1

        return index


