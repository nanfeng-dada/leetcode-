class NumArray:

    def __init__(self, nums: list):
        l=len(nums)
        self.sum=[0]*(l+1)
        for i in range(1,l+1):
            self.sum[i]=self.sum[i-1]+nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j+1]-self.sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)