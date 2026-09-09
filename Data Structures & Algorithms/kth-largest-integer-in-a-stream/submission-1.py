import bisect 


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = []

        for num in nums:
            bisect.insort_left(self.nums, num)

        self.k = k


    def add(self, val: int) -> int:
        print(self.nums)
        print(self.k)
        print(val)
        
         
        bisect.insort_left(self.nums, val)
        
        index = len(self.nums) - self.k


        return self.nums[index]
        
