class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        while l < r:
            mid = l + (r-l) // 2
            if arr[mid] >= x: 
                r = mid
            else: 
                l = mid + 1
        # print(l)
        # l is index of first elem >= x
        r = l
        l = r-1
        # print(arr[l])
        # print(arr[r])

        res = deque([])

        while len(res) < k:
            if l < 0 and r >= len(arr): 
                return res
            elif l < 0 or (not r >= len(arr) and abs(x - arr[r]) < abs(x - arr[l])):
                res.append(arr[r])
                r += 1
            else:
                res.appendleft(arr[l])
                l -= 1
            
        return list(res)
