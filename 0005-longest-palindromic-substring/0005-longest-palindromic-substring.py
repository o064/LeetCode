class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        start = 0
        n =len(s)
        for i in range(n):
            l , r = i,i
            while l >= 0 and r < n and s[l] == s[r] :
                if (r-l+1) > maxLen: 
                    maxLen = r-l+1
                    start=l
                l -=1
                r +=1
            l , r = i,i+1
            while l >= 0 and r < n and s[l] == s[r] :
                if (r-l+1) > maxLen: 
                    maxLen = r-l+1
                    start=l
                l -=1
                r +=1
        return s[start : start + maxLen]

            
