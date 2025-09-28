class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for s in range(n-m+1):
            if needle == haystack[s : s+m]:
                return  s
        return -1
        