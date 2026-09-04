from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)
        for c in s: 
            counts[c] += 1

        t_counts = defaultdict(int)
        for c in t: 
            t_counts[c] += 1

        return counts == t_counts
