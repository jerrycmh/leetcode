class Solution:
    def leafTravel(self, root):
        result = []
        if root.left == None and root.right == None:
            return [root.val]
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left == None and node.right == None:
                result.append(node.val)
            else:
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
        return result
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf1 = self.leafTravel(root1)
        leaf2 = self.leafTravel(root2)
        return leaf1 == leaf2