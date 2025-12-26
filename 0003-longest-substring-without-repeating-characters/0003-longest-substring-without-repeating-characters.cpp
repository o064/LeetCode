class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n =s.size();
        if(n == 0 || n == 1)
            return n ;
        int l = 0; 
        int r = 1; 
        int maxLen = 1 ;
        set<char> mySet;
        mySet.insert(s[l]);
        while(r < n ){
            if(mySet.count(s[r])){
                while(s[l] != s[r]){
                    mySet.erase(s[l]);
                    l++;
                }
                l++;
            }else 
                mySet.insert(s[r]);
        
            maxLen = max(maxLen , r-l+1);
            r++;
        }

        return maxLen;

    }
};