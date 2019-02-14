# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        
        self.count = 0
        
        def helper(node):
            if not node:
                return
            
            left = helper(node.left)
            right = helper(node.right)
            
            if (not left or left == node.val) and (not right or right == node.val ):
                self.count += 1
                return node.val
            
            return '//'
        
        helper(root)
        return self.count