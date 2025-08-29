class Solution:
    def countSubstrings(self, s: str) -> int:
        n =len(s)
        self.res = 0 
        def helper(l,r):
            while l >=0 and r < n and s[l] == s[r]:
                self.res += 1
                l -= 1
                r +=1 
        for i in range(n):
            helper(i,i)
            helper(i,i+1)
        return self.res
