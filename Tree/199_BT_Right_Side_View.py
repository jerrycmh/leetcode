# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = []
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = []
        visited, stack = [], [(root, 0)]
        
        while stack:
            node, level = stack.pop()
            if level not in visited:
                result.append(node.val)
                visited.append(level)
            if node.left: stack.append((node.left, level+1))
            if node.right: stack.append((node.right, level+1))
            
        return result