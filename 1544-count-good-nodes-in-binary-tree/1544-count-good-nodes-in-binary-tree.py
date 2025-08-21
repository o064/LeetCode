# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maPrev = root.val
        self.goodNodes = 0
        def countGood(root ,maxPrev):
            if not root : 
                return 
            if root.val >= maxPrev:
                maxPrev=root.val
                self.goodNodes +=1 
            countGood(root.left, maxPrev)
            countGood(root.right,maxPrev)
        countGood(root ,maPrev )
        return self.goodNodes
        