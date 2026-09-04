class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = set(["+", "-", "*", "/"])

        for token in tokens: 
            # print("Stack: ")
            # print(stack)
            # print("Token: "+ token)
            if token in operators: 
                b = int(stack.pop(-1))
                a = int(stack.pop(-1))

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a*b)
                elif token == "/":
                    stack.append(int(a/b))
            else:
                stack.append(token)

        return int(stack.pop(-1))
