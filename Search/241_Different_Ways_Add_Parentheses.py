class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in '+-*':
                prev = self.diffWaysToCompute(input[:i])
                post = self.diffWaysToCompute(input[i+1:])
                for n in prev:
                    for m in post:
                        res.append(self.operation(n, m, input[i]))
        return res
    
    def operation(self, m, n, op):
        if op == '+':
            return m+n
        if op == '-':
            return m-n
        if op == '*':
            return m*n