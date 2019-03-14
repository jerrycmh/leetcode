class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        result = [0]
        
        def helper(root):
            if not root:
                return -1
            left = helper(root.left)
            right = helper(root.right)
            
            result[0] = max(result[0], left+right+2)
            return max(left+1, right+1)
        
        helper(root)
        return result[0]