# 动态规划
class Solution:
    def rob(self, nums: list) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        l = len(nums)
        dp = [0] * l
        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2, l):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[l - 1]

if __name__=='__main__':
    a=Solution()

    print(a.rob([2,1,1,2]))