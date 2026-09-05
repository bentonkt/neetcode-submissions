class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        
        while True: 
            running = 0
            while num // 10: 
                running += (num % 10) ** 2
                num = num // 10
            running += (num % 10) ** 2
            num = num // 10
            print(running)
            if running == 1: 
                return True
            if running in seen: 
                return False
            seen.add(running)

            num = running

        return True

