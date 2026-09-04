class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        biggest = 0
        while len(hashset) > 0:
            elem = hashset.pop()
            up = elem
            down = elem
            while up + 1 in hashset:
                up += 1
                hashset.remove(up)
            while down - 1 in hashset:
                down -= 1
                hashset.remove(down)
            size = up - down + 1
            biggest = max(size, biggest)
        
        return biggest