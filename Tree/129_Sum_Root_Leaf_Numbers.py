class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = []
        stack = [(root, root.val)]
        
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                result.append(path)
            if node.left: stack.append((node.left, path*10+node.left.val))
            if node.right: stack.append((node.right, path*10+node.right.val))
            
        return sum(result)