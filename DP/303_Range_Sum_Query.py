class NumArray:

    def __init__(self, nums: List[int]):
        self.array = [0 for _ in range(len(nums)+1)]
        for i in range(1, len(self.array)):
            self.array[i] = self.array[i-1] + nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.array[j+1]-self.array[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)