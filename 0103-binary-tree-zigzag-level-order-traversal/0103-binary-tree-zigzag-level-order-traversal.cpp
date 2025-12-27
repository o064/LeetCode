/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if(!root) return {};
        vector<vector<int>> res;
        queue<TreeNode*> q; 
        q.push(root);
        bool dir = 0;
        while(!q.empty()){
            auto size = q.size();
            vector<int> lvl;
            for(int i = 0 ; i < size ; i++){
                auto node = q.front();
                lvl.push_back(node->val);
                q.pop();
                if(node->left)
                    q.push(node->left);
                if(node->right)
                    q.push(node->right);

            }
            if(dir) reverse(lvl.begin(), lvl.end());
            dir = !dir;
            res.push_back(lvl);
        }
        return res; 
    }
};