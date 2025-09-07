class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True 
        maxLen = 0
        for w in wordDict :
            maxLen = max(maxLen , len(w))
        wordDict = set(wordDict)
        for i in range(1 , n+1):
            for j in  range(i  - 1 ,max(-1 , i - maxLen - 1 ) , -1):
                if dp[j] and s[j: i ] in wordDict :
                    dp[i]= True
        return dp[-1]