# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.result = 0
        covered = {None}
        
        def dfs(node, parent = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                
                if (parent is None and node not in covered or node.left not in covered or node.right not in covered):
                    self.result += 1
                    covered.update({node, parent, node.left, node.right})
        
        dfs(root)
        return self.result