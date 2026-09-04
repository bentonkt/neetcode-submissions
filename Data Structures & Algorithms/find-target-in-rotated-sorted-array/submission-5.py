class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        


        def helper(l, r): # Left and right bounds, inclusive
            print(l)
            print(r)
            if l == r and nums[r] != target:
                return -1
            mid = (r+l) // 2
            print(mid)
            if nums[mid] == target:
                return mid
        
            if nums[mid] < nums[0]:
                # We're in the right portion of the array
                if target < nums[mid] or (target > nums[mid] and target >= nums[0]):
                    return helper(l, mid-1)
                else:
                    return helper(mid+1, r)
            else:
                # We're in the left portion of the array
                if target > nums[mid] or (target < nums[mid] and target < nums[0]): 
                    return helper(mid+1, r)
                else:
                    return helper(l, mid-1)


        return helper(0, len(nums)-1)
