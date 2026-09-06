class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1

        while l <= r: 
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l+r) // 2

            if nums[mid] < nums[mid-1]:
                return nums[mid]

            if nums[mid] < nums[r]: 
                r = mid - 1
            elif nums[mid] >= nums[l]:
                l = mid + 1

            

