class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums[0], nums[1])
        
        # We know an element is the minimum if the elements on either side of it are greater than it

        # Find the value at the middle
        mid = len(nums) // 2
        if nums[mid] < nums[mid-1] and nums[mid] < nums[mid +1]:
            return nums[mid]

        # Check the ends of the array
        start = nums[0]
        end = nums[-1]


        if nums[mid] > end:
            # Then the min must be to the right
            return self.findMin(nums[mid+1:])
        else: 
            # The min must be to the left
            return self.findMin(nums[:mid])
                

