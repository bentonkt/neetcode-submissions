class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        elems = path.split("/")

        for elem in elems: 
            print(elem)
            if elem == ".":
                continue
            elif elem == "..":
                if stack:
                    stack.pop()
            elif elem == "":
                continue
            else: 
                stack.append("/" + elem)

        return "".join(stack) if stack else "/"