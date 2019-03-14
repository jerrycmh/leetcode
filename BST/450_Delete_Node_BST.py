# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        if key > root.val: root.right = self.deleteNode(root.right, key)
        elif key < root.val: root.left = self.deleteNode(root.left, key)
        else:
            if not root.right: return root.left
            if not root.left: return root.right
            temp = root.right
            while temp:
                m = temp.val
                temp = temp.left
            root.val = m
            root.right = self.deleteNode(root.right, m)
        return root 