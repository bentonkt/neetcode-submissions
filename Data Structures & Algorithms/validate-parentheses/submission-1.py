class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '{', '[']
        stack = []

        for c in s:
            if c in opening:
                stack.append(c)
            elif not stack:
                return False
            elif c == ']':
                if stack[-1] != '[':
                    return False
                stack.pop()
            elif c == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()
            elif c == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
            else:
                return False
            
        return not stack