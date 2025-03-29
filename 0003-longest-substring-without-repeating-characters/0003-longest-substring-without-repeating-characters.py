class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=r=maxLen= 0
        mySet = set()
        while r < len(s): 
            while l < r and s[r] in mySet :
                mySet.remove(s[l]) 
                l +=1    
            mySet.add(s[r])
            r +=1
            maxLen = max(maxLen, r-l)

        return maxLen
            
                
        #  set , l ,r
        