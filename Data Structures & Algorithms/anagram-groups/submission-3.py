class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            freqs = [0] * 26
            # Get the number frequency
            for c in s:
                index = ord(c) - ord('a')
                freqs[index] += 1

            anagrams[tuple(freqs)].append(s)

        return list(anagrams.values())