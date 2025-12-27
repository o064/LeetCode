class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res ;
        map< vector<int> , vector<string> > mp;

        for(auto & str : strs){

            vector<int> freq(26,0);

            for(auto & c :str)
                freq[c - 'a']++;

            
            mp[freq].push_back(str);

        }

        for(auto& p  : mp){
            res.push_back(p.second);
        }

        return res;



        return res ;
    }
};