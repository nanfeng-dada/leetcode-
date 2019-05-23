# 法1、老老实实一步步移，采用pop和insert
# 法2、pythonic做法
# 法3、将数组分为两部分，分为0——nums.size()-k-1和nums.size()-k——nums.size()-1; 两部分分别反转，再整体反转，就能得到正确的结果。
# 例子：[1,2,3,4,5,6,7] 和 k = 3 分为[1,2,3,4]和[5,6,7];分别反转后得到[4,3,2,1,7,6,5] 再整体反转得[5,6,7,1,2,3,4] 即为正确得结果
# 法4、循环交换
class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        nums[:]=nums[n-k:]+nums[:n-k]