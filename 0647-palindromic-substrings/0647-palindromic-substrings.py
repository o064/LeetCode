class Solution:
    def countSubstrings(self, s: str) -> int:
        n =len(s)
        dp = [ [False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] =True
        res = n
        for L in range(2,n+1):
            for i in range(n-L+1):
                j = i + L -1
                if L == 2:
                    dp[i][j] = (s[i] == s[j])
                else :
                    dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])
                if dp[i][j] : 
                    res += 1
        return res        