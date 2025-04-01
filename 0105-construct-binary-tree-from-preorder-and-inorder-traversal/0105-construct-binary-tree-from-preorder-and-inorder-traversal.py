# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if inorder:
            Index = inorder.index(preorder.pop(0))
            root =TreeNode(inorder[Index] )
            root.left = self.buildTree(preorder , inorder[:Index])
            root.right = self.buildTree(preorder , inorder[Index+1 :])
            return root
