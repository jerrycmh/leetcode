class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            if node.right: stack.append((node.right, level+1))
            if node.left: stack.append((node.left, level+1))
        
        return result[::-1]