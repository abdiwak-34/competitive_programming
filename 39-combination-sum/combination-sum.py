class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        def dfs(i, cur, sums):
            if sums == target:
                result.append(cur[:])
                return
            
            if sums > target or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i, cur, sums + candidates[i])
            cur.pop()
            dfs(i+1, cur, sums)

        dfs(0, [], 0)
        return result