# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            root = TreeNode(val)
            return root
        
        node = root
        while True:
            if val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
        return root