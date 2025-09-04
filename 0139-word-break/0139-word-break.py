class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: 
        n =len(s)
        dp = [False] * (n+1)
        dp[0] = True

        mySet = set(wordDict)

        maxLen= 0 
        for w in wordDict:
            maxLen = max(maxLen , len(w))
    
        for i in range (1, n  + 1):
            lb = max(0, i - maxLen) 
            for j in range(i - 1 ,lb - 1  , -1 ):
                if  dp[j] and s[j:i] in mySet :
                    dp[i] = True
                    break
        return dp[n]
                
                




