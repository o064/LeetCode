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
    vector<vector<int>> levelOrder(TreeNode* root) {
         /* res is vector of vector  each vector is level 
            i need queue to do bfs 
            when level is end i will make need vector 
            at each level i will pop the element then push all it is childrens in the queue
            push the left child first to be from left to right 

            while q is not empty 
            pop the front 
            push it is childres 


         */
        if(!root)
            return {};
        vector<vector<int>> res ;
        queue<TreeNode* > q ; 
        q.push(root);

        while(!q.empty()){
            int size  = q.size();
            vector<int>lvl ;
            for(int i = 0 ; i < size ; i++){
                TreeNode* node = q.front();
                lvl.push_back(node->val);       
                q.pop();
                if (node->left)
                    q.push(node->left);
                if(node->right)
                    q.push( node->right);
            }
            res.push_back(lvl);

        }


         return res ; 
        
    }
};