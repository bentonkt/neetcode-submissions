class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Get value counts for s1
        map1 = defaultdict(int)
        for c in s1: 
            map1[c] += 1
        # Now see if any substring has matching value counts
        map2 = defaultdict(int)
        for i in range(len(s2) - len(s1) + 1):
            if i == 0:
                for c in range(i, i + len(s1)):
                    map2[s2[c]] += 1
            else:
                if map2[s2[i-1]] == 1:
                    map2.pop(s2[i-1])
                else:
                    map2[s2[i-1]] -= 1
                    print("test")
                map2[s2[i+len(s1)-1]] += 1

            if map1 == map2: 
                return True

        return False