class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        i = len(digits) - 1
        while i >= 0: 
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            digits[i] = 0

            i -= 1

        res = [1]
        res.extend(digits)

        return res