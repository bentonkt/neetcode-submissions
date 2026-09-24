class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        summ = sum(matchsticks)

        if summ % 4 != 0:
            return False

        target = summ / 4

        sides = [0, 0, 0, 0]

        def dfs(index):
            if sum(sides) == summ: 
                return True
            match = matchsticks[index]
            for i in range(4):
                # Put it in this sides
                if sides[i] + match > target:
                    continue

                sides[i] += match
                if dfs(index + 1):
                    return True
                sides[i] -= match

            return False

        return dfs(0)



