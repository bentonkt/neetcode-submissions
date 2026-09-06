class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures): 
            while stack: 
                if temp > stack[-1][0]: 
                    newTemp, index = stack.pop()
                
                    res[index] = i - index

                else: 
                    break

            stack.append((temp, i))


        return res