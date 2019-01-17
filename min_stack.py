class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_arr = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.min_arr.append(x)
        self.min_arr = sorted(self.min_arr)
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        ele = self.stack.pop()
        self.min_arr.remove(ele)
        

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        else:
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_arr[0]