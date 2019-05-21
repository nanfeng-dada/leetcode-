# 给定一个排序数组，你需要在原地删除重复出现的元素，
# 使得每个元素只出现一次，返回移除后数组的新长度。
# 由于使用引用传回，必须修改nums自身指向
# my solution
class Solution:
    def removeDuplicates(self, nums: list):
        myset = sorted(list(set(nums)))
        l = len(myset)
        nums[:l] = myset[:l]
        return l

#对于上述解法：set后list操作会使得有序数组顺序变化，需要重新排序
# 下面的解法基于该方法修改，
class Solution1:
    def removeDuplicates(self, nums: list) -> int:
        def dedupe(items):
            seen = set()

            for item in items:
                if item not in seen:
                    yield item
                    seen.add(item)

        index = 0
        for ele in dedupe(nums):
            nums[index] = ele
            index += 1

        return index
# 更简单的切片处理方式:
class Solution4:
    def removeDuplicates(self, nums: list) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

# 网友的骚操作
class Solution3:
    def removeDuplicates(self, nums: list) -> int:
        distinct_nums = sorted(list(set(nums)))
        nums.clear()
        nums.extend(distinct_nums)
        return len(nums)
"""
#下面为不用python set()函数的解法：
# 采用两个游标，遍历一遍
# 遗憾的是这种方法还有有set+排序+切片 快
"""

class Solution2:
    def removeDuplicates(self, nums: list) -> int:
        # 特殊情况处理
        if not nums:
            return 0
        # 设置两个游标，前面的游标用于找第一个不重复的数
        # 后一个游标用来重新定位去重数组的索引
        cur_next=0
        # 前一个游标从一开始，因为第0个数字一定要存在去重数组里
        for cur_first in range(1,len(nums)):
            if nums[cur_next]<nums[cur_first]:
                cur_next+=1
                nums[cur_next]=nums[cur_first]
        #返回的数组长度比最后一个索引值大1
        return cur_next+1




if __name__=='__main__':

    a=Solution4()

    print(a.removeDuplicates([-1,1,2,2]))