class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            result.append(node.val)
            helper(node.right)
        
        helper(root)
        m = min(abs(a-b) for a,b in zip(result[:-1], result[1:]))
        return m