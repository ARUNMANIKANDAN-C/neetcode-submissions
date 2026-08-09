class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        comb = []
        candidates.sort()

        def backtrack(path, start, total):
            
            if total == target:
                comb.append(path[:])
                return

            for i in range(start, len(candidates)):

                if total + candidates[i] > target:
                    break

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])

                backtrack(path, i + 1, total + candidates[i])

                path.pop()

        backtrack([], 0, 0)

        return comb