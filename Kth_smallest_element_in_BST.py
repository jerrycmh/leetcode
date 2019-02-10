class Solution:
    def kthSmallest(self, root: 'TreeNode', k: 'int') -> 'int':
        if not root:
            return []
        
        res = []
    
        def helper(node, k):
            if node:
                helper(node.left, k)
                if len(res) != k:
                    res.append(node.val)
                helper(node.right, k)
        
        helper(root, k)
        return res[-1]