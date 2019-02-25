class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        swap = [0 for _ in range(len(A))]
        keep = [0 for _ in range(len(A))]
        
        swap[0] = 1
        keep[0] = 0
        
        for i in range(1, len(A)):
            keep[i], swap[i] = float('inf'), float('inf')
            if A[i] > A[i-1] and B[i] > B[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1]+1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                keep[i] = min(swap[i-1], keep[i])
                swap[i] = min(keep[i-1]+1, swap[i])
        
        return min(swap[-1], keep[-1])