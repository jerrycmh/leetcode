class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        nums = [i for i in range(len(S)+1)]
        lo, hi = 0, len(nums)-1
        res = []
        
        for c in S:
            if c == 'I':
                res.append(nums[lo])
                lo += 1
            else:
                res.append(nums[hi])
                hi -= 1
        
        res.append(hi)
        return res