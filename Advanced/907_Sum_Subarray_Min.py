class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        
        stack = []
        ans, dot = 0, 0
        for i, num in enumerate(A):
            cnt = 1
            while stack and stack[-1][0] >= num:
                n, c = stack.pop()
                cnt += c
                dot -= n*c
            
            stack.append((num, cnt))
            dot += num * cnt
            ans += dot
        
        return ans % MOD