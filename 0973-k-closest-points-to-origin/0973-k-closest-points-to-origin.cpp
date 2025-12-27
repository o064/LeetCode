class Solution {
public:
    int calcDistance(int x , int y){
        return (x*x + y*y);
    }
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int,vector<int>>, vector<pair<int,vector<int>>>, greater<pair<int,vector<int>>>> pq;
        for(auto & p : points)
            pq.push(make_pair(calcDistance(p[0],p[1]) , p));

        vector<vector<int>> res;
        while(k){
            res.push_back(pq.top().second);
            pq.pop();
            k--;
        }

        return res;
        
    }
};