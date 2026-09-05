class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        current = s[0]
        window = defaultdict(int)
        for r in range(len(s)): 
            # Update count
            window[s[r]] += 1

            # check if this is the most frequent char in the window now
            if window[s[r]] > window[current]:
                current = s[r]
            
            # Make sure there are at most k replacements
            total = sum(window.values()) - window[current]
            while total > k: 
                total -= window[s[l]]
                window[s[l]] -= 1
                l += 1

            res = max(r-l+1, res)

        return res