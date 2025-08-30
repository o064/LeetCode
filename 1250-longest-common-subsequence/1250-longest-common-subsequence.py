class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cols = len(text1)+1
        rows = len(text2)+1
        dp = [[0]*cols for _ in range(rows)]

        for row in range(1,rows):
            for col in range(1,cols):
                if text1[col-1] == text2[row-1]:
                     dp[row][col] = 1 + dp[row-1][col-1]
                else : 
                    dp[row][col] = max(dp[row][col-1] ,  dp[row-1][col])
        return dp[-1][-1]
