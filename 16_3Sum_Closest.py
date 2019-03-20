class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        
        nums.sort()
        result = nums[0]+nums[1]+nums[2]
        
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                tmp = nums[j]+nums[k]+nums[i]
                if tmp == target:
                    result = tmp
                    break
                if abs(tmp-target) < abs(result-target):
                    result = tmp
                if tmp > target:
                    k -= 1
                elif tmp < target:
                    j += 1
        return result