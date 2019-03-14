class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = root
        while node:
            if node.val == val:
                return node
            elif val > node.val:
                node = node.right
            else:
                node = node.left
        
        return None