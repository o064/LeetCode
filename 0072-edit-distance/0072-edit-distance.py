class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n= len(word2)
        dp = [[-1] * (n+1) for _ in range(m+1)]
        def rec(m,n):
            if m == 0:
                return n
            if n == 0 :
                return m 
            if dp[m][n] != -1 :
                return dp[m][n]
            if word1[m-1] == word2[n-1]:
                dp[m][n] = rec(m-1,n-1) #matched
                return dp[m][n]
            dp[m][n]= 1 + min(
                rec(m-1,n-1), # replace
                rec(m,n-1), # insert
                rec(m-1,n) # del
            )
            return dp[m][n]
        return rec(m,n)