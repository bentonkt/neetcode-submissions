class Solution:
    def value_counts(self, string):
        res = [0] * 26 
        for i, c in enumerate(string): 
            pos = ord(c) - ord('a')
            res[pos] = int(res[pos]) + 1
        return str(res)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs: 
            h = self.value_counts(s)
            groups[h].append(s)


        return list(groups.values())
    