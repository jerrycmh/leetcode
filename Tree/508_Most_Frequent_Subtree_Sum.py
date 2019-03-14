# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.graph = {}
        
        def helper(node):
            if not node: return 0
            s = node.val + helper(node.right)+helper(node.left)
            if s not in self.graph:
                self.graph[s] = 1
            else:
                self.graph[s] += 1
            
            return s
        
        helper(root)
        counter = 0
        result = []
        for key, value in self.graph.items():
            if value > counter:
                counter = value
        for key, value in self.graph.items():
            if self.graph[key] == counter:
                result.append(key)
        return result