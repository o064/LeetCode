class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        if m > n:
            return -1

        d = 256
        q = 101 

        h = pow(d,m-1)%q
        p = t = 0 
        for  i in range(m):
            p =(d * p+ ord(needle[i]))%q
            t =(d * t+ ord(haystack[i]))%q

        for s in range(n-m+1):
            if p == t :
                if needle == haystack[s:s+m]:
                    return s
            if  s <  n - m :
                t = (d * (t - ord(haystack[s]) * h) + ord(haystack[s+m]))%q
                if t < 0 :
                    t  += q 
        return -1

