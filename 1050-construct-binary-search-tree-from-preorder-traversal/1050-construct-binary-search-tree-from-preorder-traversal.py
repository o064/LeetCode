# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            node = TreeNode(val)
            if stack[-1].val > val :
                stack[-1].left = node
            else : 
                parent =None 
                while stack and stack[-1].val < val:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)
        return root 

            
            



        