# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if not root:
            self.arr = []
        else:
            self.arr = sorted(self.bFS(root))

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.arr:
            return self.arr.pop(0)
        else:
            return None
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.arr:
            return True
        else:
            return False
    
    def bFS(self, root):
        result = [root.val]
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                result.append(node.left.val)
                stack.append(node.left)
            if node.right:
                result.append(node.right.val)
                stack.append(node.right)
        return result
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()