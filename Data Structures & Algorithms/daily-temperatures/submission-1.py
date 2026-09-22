class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures): 
            if not stack:
                stack.append((temp, i))

            else: 
                if temp <= stack[-1][0]:
                    stack.append((temp, i))
                else:
                    while stack and temp > stack[-1][0]:
                        val, index = stack.pop()
                        res[index] = i - index
                    stack.append((temp, i))

        return res
