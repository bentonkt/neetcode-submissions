from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return list(sorted(s)) == list(sorted(t))
