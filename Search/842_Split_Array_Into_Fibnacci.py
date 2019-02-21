class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return []
        fib = []
        for i in range(1, len(S)):
            for j in range(i+1, len(S)):
                prev = S[:i]
                if len(prev) > 1 and prev[0] == '0' or int(prev) > 2**31-1: return []
                cur = S[i:j]
                if len(cur) > 1 and cur[0] == '0' or int(cur) > 2**31-1: break
                index = j
                fib = [int(prev), int(cur)]
                while index < len(S):
                    next_n = int(prev)+int(cur)
                    if next_n > 2**31-1: break
                    length = len(str(next_n))
                    if S[index:index+length] != str(next_n) or (S[index] == '0' and length>1):
                        break
                    else:
                        fib.append(next_n)
                        prev, cur = cur, str(next_n)
                        index += length
                if index == len(S):
                    return fib
                
        return []