class Solution:

    def __init__(self, w: List[int]):
        self.arr = []
        for i, weight in enumerate(w): 
            if i == 0: 
                self.arr.append(weight)
            else: 
                self.arr.append(self.arr[i-1] + weight)

    def pickIndex(self) -> int:
        print(self.arr)
        index = random.randint(1, self.arr[-1])
        print(index)

        l, r = 0, len(self.arr)

        while l < r: 
            mid = l + (r - l) // 2

            if self.arr[mid] >= index: 
                r = mid
            else:
                l = mid + 1

        return l

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()