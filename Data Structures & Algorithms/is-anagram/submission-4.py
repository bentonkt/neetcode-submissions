class Solution:
    def hashh(self, s):
        letters = [0] * 26

        for i, c in enumerate(s): 
            letters[ord(c) - ord('a')] += 1

        return letters

    def isAnagram(self, s: str, t: str) -> bool:

        return self.hashh(s) == self.hashh(t)

