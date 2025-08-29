class Solution {
public:
    vector<vector<int>> ans;
    vector<int> combination;
    void solve(vector<int>& candidates, int target,int index){
        if(target == 0){
            ans.push_back(combination);
            return ;
            
        }
        if(index >= candidates.size() || target < 0 )
            return ;
        
        combination.push_back(candidates[index]);
        solve(candidates,target - candidates[index] , index );
        combination.pop_back();
        solve(candidates,target, index + 1);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        solve(candidates,target , 0);
        return ans;
    }
};