import operator
class Solution(object):
    def get_operator_fn(self, op):
        return {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.div
            }[op]
    
    
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1:
            return int(tokens[0])
        size = len(tokens)
        begin = 2
        while size != 1:
            print tokens
            for i in range(begin, size):
                if tokens[i] in ["+", "-", "*", "/"]:
                    result = self.get_operator_fn(tokens[i])(float(tokens[i-2]), float(tokens[i-1]))
                    index = i-2
                    tokens.pop(i)
                    tokens.pop(i-1)
                    tokens[index] = result
                    size = len(tokens)
                    begin = index
                    break
        
        return int(tokens[0])


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        ops = {'+': operator.add, '-': operator.sub, 
               '*': operator.mul, '/': self.divide}
        
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                r = stack.pop()
                l = stack.pop()
                
                val = ops[t](l, r)
                stack.append(val)
        
        return stack[-1]
    
    def divide(self, l, r):
        if (l < 0 and r > 0) or (l > 0 and r < 0):
            return - (abs(l) // abs(r))
        else:
            return l // r