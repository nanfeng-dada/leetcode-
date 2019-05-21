# 两边哈希表
class Solution:
    def singleNumber(self, nums: list) -> int:
        dic={}
        l=len(nums)
        for i in range(l):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1
        for i in range(l):
            if dic[nums[i]]==1:
                return nums[i]
# 异或运算
class Solution1:
    def singleNumber(self, nums: list) -> int:
        ans=0
        for n in nums:
            ans=ans^n
        return ans