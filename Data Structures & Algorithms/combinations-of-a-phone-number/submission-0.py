class Solution:
    def getLetters(self, digit): 
        if digit < 7: 
            return [chr((digit-2)*3 + ord('a')), chr((digit-2)*3 + ord('a') + 1), chr((digit-2)*3 + ord('a') + 2)]
        elif digit == 7:
            return ['p', 'q', 'r', 's']
        elif digit == 8: 
            return ['t', 'u', 'v']
        else:
            return ['w', 'x', 'y', 'z']

    def helper(self, a, i):
        print(a)
        if i == len(self.digits): 
            self.res.append(a)
            return

        letters = self.getLetters(int(self.digits[i]))

        for letter in letters:
            self.helper(a + letter, i+1)


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        self.digits = digits
        self.res = []
        self.helper("", 0)

        return self.res

