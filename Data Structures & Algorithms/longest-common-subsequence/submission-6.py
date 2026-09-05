class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Optional: Swap to ensure the 1D array is the smaller dimension
        if len(text1) < len(text2):
            text1, text2 = text2, text1
            
        m, n = len(text1), len(text2)
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if text1[row] == text2[col]:
                    # Diagonal + 1 (using prev because we are moving bottom-up)
                    curr[col] = 1 + prev[col + 1]
                else:
                    # Max of right cell (curr) and bottom cell (prev)
                    curr[col] = max(curr[col + 1], prev[col])
            
            # Swap row references for the next iteration
            prev, curr = curr, prev
            
        return prev[0]
            