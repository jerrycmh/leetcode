"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        dep = 1
        stack = [(root,1)]
        
        while stack:
            node, level = stack.pop()
            dep = max(dep, level)
            
            for c in node.children:
                stack.append((c, level+1))
        
        return dep