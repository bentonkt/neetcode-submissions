class Solution:
    def atoi(self, num):
        digits = list(num)
        num_digits = len(digits)
        res = 0
        for i, digit in enumerate(digits): 
            res += int(digit) * 10 ** (num_digits - i - 1)

        return res


    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        num1_int = self.atoi(num1)
        num2_int = self.atoi(num2)

        return str(num1_int * num2_int)