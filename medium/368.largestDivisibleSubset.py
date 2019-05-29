# dp的同时记录解
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums: return nums
        if len(nums) == 1: return nums
        l = len(nums)
        nums.sort()

        dp = [[i] for i in nums]

        for i in range(1, l):
            for j in range(i):
                if not nums[i] % nums[j]:
                    dp[i] = max(dp[j] + [nums[i]], dp[i], key=len)

        return max(dp, key=len)

# 借鉴最长上升序列，dp记录的是当前最长整除子序列的长度
# 再通过遍历，条件筛选重构解
class Solution1(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums: return nums
        if len(nums) == 1: return nums
        l = len(nums)
        nums.sort()

        dp = [1] * l

        for i in range(1, l):
            for j in range(i):
                if not nums[i] % nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        maxl = max(dp)
        ans = []
        for i in range(l - 1, -1, -1):
            if maxl == dp[i]:
                if not ans:
                    ans.append(nums[i])
                    maxl -= 1
                elif not ans[-1] % nums[i]:
                    ans.append(nums[i])
                    maxl -= 1
        return ans[::-1]


if __name__=="__main__":
    a=Solution1()
    print(a.largestDivisibleSubset([10, 5, 3, 15, 20]))