class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int,int> valToIndex;

            for (int i = 0; i < nums.size(); i++) {
                int x = target - nums[i];
                auto it = valToIndex.find(x);
                if (it != valToIndex.end()) {
                    return {i, it->second};
                }
                valToIndex[nums[i]] = i;  // insert current element AFTER checking
            }

    return {};  // no solution
    }
};