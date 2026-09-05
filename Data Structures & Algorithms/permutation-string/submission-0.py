class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Get value counts for s1
        map1 = defaultdict(int)
        for c in s1: 
            map1[c] += 1

        # Now see if any substring has matching value counts

        for i in range(len(s2) - len(s1) + 1):
            map2 = defaultdict(int)
            for c in range(i, i + len(s1)):
                map2[s2[c]] += 1

            if map1 == map2: 
                return True

        return False