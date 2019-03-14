class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, cur_sum = stack.pop()
            if node.left == None and node.right == None:
                if cur_sum == sum: return True
            else:
                if node.left: stack.append((node.left, cur_sum+node.left.val))
                if node.right: stack.append((node.right, cur_sum+node.right.val))
        
        return False