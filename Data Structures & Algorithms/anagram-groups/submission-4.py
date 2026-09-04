class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for str in strs: 
            key = tuple(sorted(str))
            res[key].append(str)

        return list(res.values())