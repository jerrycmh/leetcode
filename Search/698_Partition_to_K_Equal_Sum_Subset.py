class Solution:
    def canPartitionKSubsets(self, nums, k):
        target = sum(nums)//k
        if k * target != sum(nums):
            return False

        res = []
        def backtracking(group, nums):
            if not nums:
                for i in range(k):
                    if group[i] != target: return False
                return True
            num = nums.pop()
            for i in range(k):
                if group[i]+num <= target:
                    group[i] += num
                    if backtracking(group, nums): return True
                    group[i] -= num
            nums.append(num)
            return False
        
        
        group = [0 for _ in range(k)]
        nums.sort()
        if nums[-1] > target:
            return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
            
        return backtracking(group, nums)