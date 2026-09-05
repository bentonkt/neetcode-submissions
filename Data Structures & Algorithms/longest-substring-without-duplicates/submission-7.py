class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentSet = {}
        length = 0
        res = 0
        start = 0

        for i, c in enumerate(s): 
            if c in currentSet and currentSet[c] >= start:
                # Reset
                # Find where this character last occurred
                length = i - currentSet[c]
                start = currentSet[c] + 1
                currentSet[c] = i
                
            else:
                length += 1
                
                currentSet[c] = i

            res = max(res, length)


        return res