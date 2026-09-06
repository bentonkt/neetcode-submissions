class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bin(l, r):
            print(l)
            print(r)
            print("___")
            mid = (l + r) // 2
            elem = nums[mid]

            if elem == target: 
                return mid
            if l >= r: 
                return -1

            

            if elem < target: 
                l = mid + 1
                return bin(l, r)
            return bin(l, mid-1)

        return bin(0, len(nums) - 1)