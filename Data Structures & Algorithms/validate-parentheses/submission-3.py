class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ["[", "(", "{"]
        closing = ["]", ")", "}"]
        for c in s: 
            if c in opening: 
                stack.append(c)
            else: 
                if stack:
                    opener = stack.pop()
                else: 
                    return False
                if opening.index(opener) != closing.index(c):
                    return False

        return len(stack) == 0

