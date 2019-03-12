class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def check(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return root1.val == root2.val and check(root1.left, root2.left) and check(root1.right, root2.right)
        
        if not s:
            return False
        if check(s, t): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)