class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for string in strs:
            length = str(len(string))
            result.append(length)
            result.append("\\")
            result.append(string)
        print(result)
        return "".join(result)


    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            length_chars = []
            while s[i] != "\\":
                length_chars.append(s[i])
                i += 1
            # Now s[i] = \
            length = int("".join(length_chars))
            end = i + length
            current = []
            i += 1
            while i <= end:
                current.append(s[i])
                i += 1
            words.append("".join(current))
        return words
