class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        diffs = []
        for i, x in enumerate(gas): 
            diffs.append(x - cost[i])

        a = 0
        index = None
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            a += diff

            if a < 0: 
                index = None
                a = 0
                continue
            # Start a running sum from this index if we don't have one already
            if index == None: 
                index = i


        return index


