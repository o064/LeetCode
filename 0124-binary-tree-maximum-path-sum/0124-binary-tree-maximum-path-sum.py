# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def dfs(node): 
            nonlocal res
            # return zero if node is null
            if not node :
                return  0
            # get the max left and right subTree while ignoring negatives
            left = max(dfs(node.left) , 0)
            right = max(dfs(node.right) , 0)
            # what is the max now ? prev or extending this path
            res = max(res , node.val + left + right)
            # one side will coninue 
            return node.val + max(left, right)
        dfs(root)
        return res
