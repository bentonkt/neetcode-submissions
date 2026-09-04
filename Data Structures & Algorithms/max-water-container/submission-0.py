class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxy = 0
        for i, height1 in enumerate(heights):
            for j, height2 in enumerate(heights):
                if min(height1, height2) * (abs(i - j)) > maxy:
                    maxy = min(height1, height2) * (abs(i - j))
    
        return maxy
                