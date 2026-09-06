class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r: 
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target and nums[r] >= target or (nums[mid] > nums[r] and nums[r] >= target) or (target > nums[mid] and nums[l] < nums[mid]): 
                l = mid+1
            else: 
                r = mid-1

        return -1