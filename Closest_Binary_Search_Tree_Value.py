class Solution:
    def closestValue(self, root: 'TreeNode', target: 'float') -> 'int':
        if not root:
            return 0
        
        stack = [root]
        diff, result = float('inf'), 0
        
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            
            if abs(node.val - target) < diff:
                diff = abs(node.val - target)
                result = node.val
        
        return result