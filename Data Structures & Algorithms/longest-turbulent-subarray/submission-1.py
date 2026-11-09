class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        if len(arr) <= 1: 
            return 1
        
        res = 1
        length = 1
        prevGreater = None

        for i in range(1, len(arr)):
            if length == 1: 
                if arr[i] == arr[i-1]:
                    continue
                elif arr[i] > arr[i-1]:
                    prevGreater = True
                    length = 2
                else:
                    prevGreater = False
                    length = 2
                res = max(res, length)
                continue

            if arr[i] == arr[i-1]:
                length = 1
            elif arr[i] > arr[i-1]: 
                if prevGreater:
                    length = 2
                    prevGreater = True
                else: 
                    length += 1
                    prevGreater = True
            else:
                if prevGreater:
                    length += 1
                    prevGreater = False
                else:
                    length = 2
                    prevGreater = False

            res = max(res, length)

        return res