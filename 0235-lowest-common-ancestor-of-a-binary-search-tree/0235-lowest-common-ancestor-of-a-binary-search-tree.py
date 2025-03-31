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
        # get the path to p,q
        def trackPath(node ,value,path) :
            if not node :
                return 
            path.append(node)
            if node.val == value :
                return 
            elif node.val > value :
                trackPath(node.left,value,path)
            else : 
                trackPath(node.right,value,path)

        # tack path 
        pPath =[]
        qPath =[]
        trackPath(root,p.val,pPath)
        trackPath(root,q.val,qPath) 
        # get last path match
        i =0 
        while (i < len(pPath) and i < len(qPath)) :
            if pPath[i].val != qPath[i].val : 
                break
            i +=1
        return pPath[i-1]

                