class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copy = []
        # Sort the strings
        for i, string in enumerate(strs):
            copy.append(''.join(sorted(string)))

        # Now strings are sorted, so iterate through to compare
        anagrams = {}
        for i, string in enumerate(copy):
            if string in anagrams.keys():
                anagrams[string].append(strs[i])
            else:
                anagrams[string] = [strs[i]]
        

        return anagrams.values()


