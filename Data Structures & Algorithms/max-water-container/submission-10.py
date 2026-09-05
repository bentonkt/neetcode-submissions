class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = -1
        while l < r:
            heightL, heightR = heights[l], heights[r]
            res = max(res, min(heightL, heightR) * (r - l))

            if heights[l] > heights[r]:
                r-=1
            else: 
                l+=1

        return res