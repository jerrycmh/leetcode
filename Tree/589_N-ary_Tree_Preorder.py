class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        
        def helper(node):
            if node == None:
                return
            result.append(node.val)
            for child in node.children:
                helper(child)
        
        helper(root)
        return result