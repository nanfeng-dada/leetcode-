"""coding: utf-8"""

# 暴力解法：时间复杂度不达标

# 两遍哈希表
# 执行用时 : 60 ms, 在Two Sum的Python3提交中击败了70.82% 的用户
# 内存消耗 : 14.9 MB, 在Two Sum的Python3提交中击败了5.51% 的用户
class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        # 一遍存入哈希表
        for i in range(len(nums)):
            hashmap[nums[i]]=i

        # 第二遍取值
        for i in range(len(nums)):
            num=target - nums[i]
            if num in hashmap:
                return [hashmap[num],i]

        return None

# 一遍哈希表
# 采用 #for index, num in enumerate(nums):生成索引和数据
# 执行用时 : 96 ms, 内存消耗 : 14 MB,
# 采用 # for index in range(len(nums)):生成索引和数据
# 执行用时 : 56 ms	内存消耗 13.9 MB

class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index in range(len(nums)):
            num=nums[index]
        #for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None

if __name__=='__main__':
    a=Solution2()
    print(a.twoSum([1,2,6,4],5))