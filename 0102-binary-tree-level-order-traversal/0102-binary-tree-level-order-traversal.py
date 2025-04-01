# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root :
            return []
        queue = deque()
        queue.append(root)
        result =[]
        while queue : 
            n = len(queue)
            level =[]
            for i in range(n):
                top = queue.pop()
                level.append(top.val)
                if top.left:
                    queue.appendleft(top.left)
                if top.right:
                    queue.appendleft(top.right)
            result.append(level)
        return result


