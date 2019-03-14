class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        graph = {0:1}
        total, count = 0, 0
        for n in nums:
            total += n
            if (total-k) in graph:
                count += graph[total-k]
            if total in graph:
                graph[total] += 1
            else:
                graph[total] = 1
        return count