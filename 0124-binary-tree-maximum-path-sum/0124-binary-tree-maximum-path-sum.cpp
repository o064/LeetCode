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
    int res = INT_MIN;
    int dfs(TreeNode* root){
        if (!root)
            return 0 ;
        // left path or right path
        int left = max(dfs(root->left) , 0);
        int right = max(dfs(root->right) , 0);
        // current res or extend path
        res = max(res , root->val + right + left);
        // choose one side
        return root->val + max(right ,left);
    
    }
    int maxPathSum(TreeNode* root) {
        dfs(root);
        return res;
        
    }
};