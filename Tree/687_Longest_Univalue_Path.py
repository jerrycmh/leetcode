class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0
        
        def path(node):
            if not node:
                return 0
            left = path(node.left)
            right = path(node.right)
            left_r, right_r = 0, 0
            if node.left and node.left.val == node.val:
                left_r = left+1
            if node.right and node.right.val == node.val:
                right_r = right+1
            self.result = max(self.result, left_r+right_r)
            return max(left_r, right_r)
        
        path(root)
        return self.result