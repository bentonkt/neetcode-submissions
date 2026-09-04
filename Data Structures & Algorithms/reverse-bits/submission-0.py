class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]

        reversed = ["0"] * 32

        for i in range(len(binary)): 
            reversed[i] = binary[-1 * (i+1)]


        return int("".join(reversed), 2)
