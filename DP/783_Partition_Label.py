class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        l = {c:i for i, c in enumerate(S)}
        
        index = pivot = 0
        res = []
        
        for i, c in enumerate(S):
            index = max(index, l[c])
            if i == index:
                res.append(i-pivot+1)
                pivot = i+1
        return res