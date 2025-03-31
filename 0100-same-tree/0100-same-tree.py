# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def inorder(fTree, sTree):
            if not fTree and   not sTree : 
                return True
            if not fTree or not sTree or fTree.val !=  sTree.val :
                return False
            return inorder(fTree.left,sTree.left) and inorder(fTree.right,sTree.right) 
        return inorder(p,q)
        
