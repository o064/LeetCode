class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        int l = 0 , maxLen = 0 ;
        set<char> mySet;
        for(int r =0 ; r < n ; r++){
            while(mySet.count(s[r])){
                mySet.erase(s[l]);
                l++;
            }
            mySet.insert(s[r]);
            maxLen = max(maxLen , r-l+1);
        }

        return maxLen;

    }
};