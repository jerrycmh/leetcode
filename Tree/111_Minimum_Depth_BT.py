class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        height = 0
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if not node.left and not node.right:
                return level+1
            if node.left: queue.append((node.left, level+1))
            if node.right: queue.append((node.right, level+1))
                
        return -1