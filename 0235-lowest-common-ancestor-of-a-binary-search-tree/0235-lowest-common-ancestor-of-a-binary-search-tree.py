# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def lca(node ,n1,n2):
            if not node: 
                return None;
            if node == n1 or node ==n2 :
                return node;
            
            leftsubTree =lca(node.left,n1,n2)
            rightsubTree =lca(node.right,n1,n2)

            if leftsubTree and rightsubTree :
                return node;
            return leftsubTree if leftsubTree else rightsubTree
        
        return lca(root,p,q)

                