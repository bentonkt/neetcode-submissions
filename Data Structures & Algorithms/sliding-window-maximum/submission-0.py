class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window = deque([])
        res = []

        for i, num in enumerate(nums):
            if i < k: 
                while window and num > window[-1][0]:
                    window.pop()

                # now num is <= last element
                window.append((num, i))
                
                if i == k - 1: 
                    res.append(window[0][0])

                continue
            
            while window and num > window[-1][0]:
                window.pop()

            if window and window[0][1] <= i - k:
                window.popleft()

            window.append((num, i))
            res.append(window[0][0])
            
        return res