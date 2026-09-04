class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                if len(stack) < 2:
                    return False
                e1 = stack.pop()
                e2 = stack.pop()
                stack.append(e1 + e2)
            elif token == "-":
                if len(stack) < 2:
                    return False
                e1 = stack.pop()
                e2 = stack.pop()
                stack.append(e2 - e1)
            elif token == "*":
                if len(stack) < 2:
                    return False
                e1 = stack.pop()
                e2 = stack.pop()
                stack.append(e1 * e2)
            elif token == "/":
                if len(stack) < 2:
                    return False
                e1 = stack.pop()
                e2 = stack.pop()
                stack.append(math.trunc(e2 / e1))
            else:
                stack.append(int(token))
        return stack.pop()