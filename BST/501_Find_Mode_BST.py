# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        visited = {}
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val not in visited:
                visited[node.val] = 1
            else:
                visited[node.val] += 1
            
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        
        m = 0
        for key, val in visited.items():
            m = max(m, val)
        result = []
        for key, val in visited.items():
            if val == m:
                result.append(key)
        return result