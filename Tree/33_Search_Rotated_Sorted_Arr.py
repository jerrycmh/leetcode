class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                mid = (left+right)//2
                if nums[mid] > nums[mid+1]:
                    return mid+1
                else:
                    if nums[mid] < nums[left]:
                        right = mid-1
                    else:
                        left = mid+1
        
        def bs(left, right):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return -1
        
        size = len(nums)
        if size == 0: return -1
        if size == 1: return 0 if nums[0] == target else -1
        ri = find_rotate_index(0, size-1)
        if ri == 0: return bs(0, size-1)
        else:
            if target < nums[0]:return bs(ri, size-1)
            else: return bs(0, ri)