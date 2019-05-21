# 统计频次
class Solution:
    def majorityElement(self, nums: list) -> int:
        dic={}
        l=len(nums)
        for i in range(l):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1

        for i in dic:
            if dic[i]>l/2:
                return i
# 摩尔投票法另一种解法是摩尔投票算法，这种算法的思想是：众数是出现次数最多的数，
# 众数和其他数出现的次数一一抵消后，剩下的一定就是众数，所以只需遍历一遍数组，就可以找到众数，时间复杂度是 O(n)
class Solution1:
    def majorityElement(self, nums: list) -> int:
        current = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                current = nums[i]
            if nums[i] == current:
                count += 1
            else:
                count -= 1
        return current
# 排序之后众数一定在中间nlogn
class Solution2:
    def majorityElement(self, nums: list) -> int:
        return sorted(nums)[len(nums) // 2]