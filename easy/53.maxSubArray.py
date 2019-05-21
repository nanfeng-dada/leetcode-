class Solution:
    def maxSubArray(self, nums: list) -> int:
        sums=-1
        last_max=-2<<31
        for i in range(len(nums)):
            sums=max(nums[i],sums+nums[i])
            last_max=max(sums,last_max)
        return last_max

# 重构解,取出和最大的子序列
class Solution2:
    def maxSubArray(self, nums: list) -> int:
        first=0
        last=1
        sums=-1
        last_max=-2<<31
        for i in range(len(nums)):
            if sums>0 :
                sums=sums+nums[i]
            else:
                # 重新开始记录
                sums =nums[i]
                first=i
                last=i+1

            # 更新最大值
            if sums>last_max:
                last_max=sums
                last=i+1

        # return last_max,nums[first:last]
        return last_max
# 非正规dp
class Solution3:
    def maxSubArray(self, nums: list) -> int:
        print(nums)
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
        print(nums)
        return max(nums)
# 还有一种分治法
if __name__=='__main__':
    a=Solution2()
    print(a.maxSubArray([0,5,-4,8,0,5]))