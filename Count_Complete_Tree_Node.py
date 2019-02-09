class Solution:
    def countNodes(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        
        stack = [root]
        count = 0
        
        while stack:
            node = stack.pop()
            count += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return count