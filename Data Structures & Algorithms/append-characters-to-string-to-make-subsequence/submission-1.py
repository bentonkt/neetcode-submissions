class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        pointer = 0
        for i, c in enumerate(t): 
            while pointer < len(s) and s[pointer] != c: 
                pointer += 1

            
            if pointer == len(s): 
                return len(t) - i
            else:
                pointer += 1

        return 0