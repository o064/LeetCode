class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        comb=[]
        def backtrack(target : int , idx : int):
            if target == 0:
                ans.append(comb[:])
                return

            if idx >= len(candidates) or target < 0 : 
                return
            comb.append(candidates[idx])
            backtrack(target - candidates[idx] , idx)
            comb.pop()
            backtrack(target  , idx + 1)
        backtrack(target , 0 )
        return ans
            