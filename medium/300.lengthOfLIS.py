class Solution:

    # 动态规划的思路：将 dp 数组定义为：以 nums[i] 结尾的最长上升子序列的长度
    # 那么题目要求的，就是这个 dp 数组中的最大者
    # 以数组  [10, 9, 2, 5, 3, 7, 101, 18] 为例：
    # dp 的值： 1  1  1  2  2  3  4    4

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size <= 1:
            return size
        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    # + 1 的位置不要加错了
                    dp[i] = max(dp[i], dp[j] + 1)
        # 最后要全部走一遍，看最大值
        return max(dp)
class Solution1:
    def lengthOfLIS(self, nums: list) -> int:
        maxL=0
        dp=[-1]*len(nums)
        for num in nums:
            # 二分查找，对于nums中的每一个数，查找到应该插入到dp中的位置
            # 如果num>dp[mid]说明，num应该插入dp【mid】之后，因此lo=mid+1
            # 如果num<=dp[mid]说明，num应该插入dp【mid】之前，即在序列nums中找到了比之前的数dp【mid】，更小的值，用该值替换dp【mid】即可，
            # 在while条件终止时，lo与hi应相差等，此时最新的mid==lo，
            lo,hi=0,maxL
            while lo<hi:
                mid=(lo+hi)>>1
                if dp[mid]<num:
                    lo=mid+1
                else:
                    hi=mid
            dp[lo]=num
            # 找到的插入点如果等于长度，说明是序列dp中最大的，因此需要长度加一，
            if lo==maxL:
                maxL+=1
        return maxL
if __name__=="__main__":
    a=Solution1()
    print(a.lengthOfLIS([10, 9, 2, 5, 3, 1,7, 101, 18]))