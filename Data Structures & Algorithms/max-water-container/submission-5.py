class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxy = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            volume = (r-l) * (min(heights[l], heights[r]))
            if volume > maxy:
                maxy = volume
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        
        return maxy
                
