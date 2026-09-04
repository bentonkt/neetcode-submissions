class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = float('-inf')

        l, r = 0, len(heights) - 1

        while l < r: 
            area = min(heights[l], heights[r]) * (r-l)
            res = max(area, res)

            if heights[l] < heights[r]:
                l+=1
                # print("l: " + str(heights[l]) + ", r: " + str(heights[r]))
            else:
                r -= 1
                # print("l: " + str(heights[l]) + ", r: " + str(heights[r]))

        return res