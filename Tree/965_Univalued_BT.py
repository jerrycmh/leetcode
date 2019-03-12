class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        value = root.val
        def helper(node):
            if not node:
                return True
            if node.val != value:
                return False
            return helper(node.left) and helper(node.right)
        
        return helper(root)