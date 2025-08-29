class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        dp = [[False] * n for _ in range(n)]  # 2D array initialized with false
        for i in range(n):
            dp[i][i] = True   # set diagonal to True  -> single ch  is palidrome
        maxLen = 1
        start = 0
        for L in range(2,n+1) :
            for i in range(n-L+1) : 
                j = i + L - 1
                if L == 2:
                    dp[i][j] = (s[i]==s[j])
                else : 
                    dp[i][j] = (s[i]==s[j] and dp[i+1][j-1])
                if dp[i][j] and L > maxLen:
                    maxLen = L
                    start = i 
        return s[start : start + maxLen]






            
