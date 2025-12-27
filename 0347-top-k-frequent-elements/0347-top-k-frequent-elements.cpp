class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mp ; // map num to freq
        for(auto num : nums) mp[num]++;
        

        priority_queue<pair<int,int> ,vector<pair<int,int>>, greater<pair<int,int>> > pq;// freq, number
        for(auto& [key, value] : mp){
            pq.push({value,key});
            if(pq.size() > k) pq.pop();
        }


        vector<int>res;
        while(k){
            res.push_back(pq.top().second);
            pq.pop();
            k--;
        }
        reverse(res.begin(), res.end());

        return res;
            
    }
};