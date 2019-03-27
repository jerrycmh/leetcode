class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(s, tmp, result):
            if s == target:
                tmp.sort()
                if tmp not in result:
                    result.append(tmp)
                return
            
            for n in candidates:
                if s+n <= target:
                    dfs(s+n, tmp+[n], result)
        
        dfs(0, [], result)
        return result