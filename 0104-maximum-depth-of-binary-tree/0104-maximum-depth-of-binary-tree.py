# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def recursion(node):
            if  node is None:
                return 0 ; 
            leftdep = recursion(node.left)
            rightdep = recursion(node.right)
            return max(leftdep,rightdep) + 1 ; 
        return recursion(root)

        