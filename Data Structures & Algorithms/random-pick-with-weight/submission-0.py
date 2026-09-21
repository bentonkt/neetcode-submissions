class Solution:

    def __init__(self, w: List[int]):
        self.arr = []
        for i, weight in enumerate(w): 
            self.arr.extend([i] * weight)

    def pickIndex(self) -> int:
        index = random.randint(0, len(self.arr)-1)

        return self.arr[index]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()