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
    int  helper(TreeNode* root , int current){
        if(root ==NULL){
            return 0;
        }
        current = current *10 +  root->val;
        if(root->left == NULL && root ->right == NULL){
            return current;
        }
        int left =helper(root->left, current);
        int right =helper(root->right, current);
        return left + right ;
    }
    int sumNumbers(TreeNode* root) {
        return helper(root ,0);
    }
};