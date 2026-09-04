class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfreqs = defaultdict(int)

        # Get character frequencies of first
        for c in s:
            sfreqs[c] += 1
        
        tfreqs = defaultdict(int)

        for c in t:
            tfreqs[c] += 1

        return sfreqs == tfreqs