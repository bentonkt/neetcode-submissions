class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        i = 0
        res = []

        for i in range(len(asteroids)): 

            
            
            if asteroids[i] > 0: 
                res.append(asteroids[i])
            else:
                # negative
                if len(res) == 0 or res[-1] < 0: 
                    res.append(asteroids[i])
                else: 
                    # collision
                    while res and res[-1] > 0 and res[-1] < - asteroids[i]:
                        res.pop()

                    if not res: 
                        res.append(asteroids[i])
                    elif res[-1] == -asteroids[i]:
                        res.pop()
                    elif res[-1] > -asteroids[i]:
                        continue
                    else: 
                        res.append(asteroids[i])


        return res
                    