class Solution:

    def encode(self, strs: List[str]) -> str:

        lens = [str(len(s)) + "|" + s for s in strs]
        return "".join(lens)


    def decode(self, s: str) -> List[str]:
        print(s)
        strs = []
        i = 0
        while i < len(s): 
            # Get num
            num = 0
            while s[i] != "|":
                num = num * 10 + int(s[i])
                i += 1
            strs.append(s[i+1:i+1+num])
            i += num + 1

        return strs