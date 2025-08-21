# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        decoded = [] 
        def preOrder(root):
            if not root :
                decoded.append('N')
                return

            decoded.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)
        return ",".join(decoded)

            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")

        self.i = 0
        def preOrder():
            if data[self.i] == 'N':
                self.i+=1
                return None
            node = TreeNode(int(data[self.i]))
            self.i+=1 
            node.left =preOrder()
            node.right =preOrder()
            return node
        return preOrder()
            

                


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))