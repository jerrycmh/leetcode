# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        inorder = []
        
        def helper(node):
            if not node: return
            helper(node.left)
            inorder.append(node.val)
            helper(node.right)
        
        helper(root)
        
        l, r = 0, len(inorder)-1
        while l < r:
            if inorder[l]+inorder[r] < k:
                l += 1
            elif inorder[l]+inorder[r] >k :
                r -= 1
            else:
                return True
        return False