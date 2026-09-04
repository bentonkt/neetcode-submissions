class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        i = 0
        while i < len(strs):
            freq1 = get_freq(strs[i])
            group = []
            j = i
            while j < len(strs):
                if freq1 == get_freq(strs[j]):
                    group.append(strs.pop(j))
                else:
                    j += 1
            groups.append(group)


        return groups

def compare(d1, d2):
    for key in d1.keys():
        if key not in d2.keys():
            return False
        if d1[key] != d2[key]:
            return False

    return True

def get_freq(string):
    freq = {}
    for c in string:
        if c in freq.keys():
            freq[c] += 1
        else: 
            freq[c] = 1
    return freq