class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        def helper(node):
            if not node:
                return
            for child in node.children:
                helper(child)
            result.append(node.val)
        
        helper(root)
        return result