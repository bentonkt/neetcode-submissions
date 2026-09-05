class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxHeight = 0

        res = 0

        while l < r:
            left = height[l]
            right = height[r]

            minimum = min(left, right)

        



            if height[l] > height[r]:
                
                amount = max(0, maxHeight - height[r])
                r-=1
                res += amount
            else: 
                
                amount = max(0, maxHeight - height[l])
                l+=1
                res += amount



            # Update the maxheight 
            maxHeight = max(maxHeight, minimum)


        return res