class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols =len(matrix[0])
        directions =[(0,-1),(0,1),(1,0),(-1,0)]
        dp = [[-1]* cols for _ in range(rows)]
        def dfs(r,c, prev_val):
            if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] <= prev_val : # base case out of bound or none increase seq
                return 0 
            if dp[r][c] != -1 :
                return  dp[r][c]
            maxLen =1
            for dr,dc in directions : 
                rn , cn = r+dr , c+dc
                maxLen = max(maxLen,1+dfs(rn,cn ,matrix[r][c]))
            dp[r][c] = maxLen
            return dp[r][c]
        ans = 0 
        for row in range(rows) :
            for col in range(cols) :
                ans = max(ans, dfs(row,col,-1))
        return ans


            
                
        