class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            length = len(s)
            res.append(str(length) + '|' + s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Get the length of the string first
            start = i
            while s[i] != '|':
                i += 1
            length = s[start:i]
            print(length)

            # Increment i to get to the start of the word
            i += 1
            word = s[i: i + int(length)]
            i += int(length)
            res.append(word)

        return res

