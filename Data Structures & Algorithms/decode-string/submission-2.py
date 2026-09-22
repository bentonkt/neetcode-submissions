class Solution:
    def decodeString(self, s: str) -> str:
        res = []

        
        def bracket(num, i):

            stack = []
            while i < len(s): 
                char = s[i]

                if char == "]":
                    return stack * num, i
                elif char.isdigit():
                    number = [char]
                    i+=1
                    while i < len(s) and s[i].isdigit():
                        number.append(s[i])
                        i+=1
                    mult = int("".join(number))
                    val, j = bracket(int(mult), i+1)
                    i= j
                    stack.extend(val)
                else:
                    stack.append(char)
                i += 1

            return stack, i

        res = bracket(1, 0)

        return "".join(res[0])