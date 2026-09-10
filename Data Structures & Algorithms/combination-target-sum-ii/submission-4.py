class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start: int, path: list[int], goal: int):
            if goal == 0:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                # Early stopping: remaining numbers are too large
                if candidates[i] > goal:
                    break
                
                # Skip duplicate elements at the same decision level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, path, goal - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return res




