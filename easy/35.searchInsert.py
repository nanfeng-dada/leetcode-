class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        # 两种target大于最大值的判断
        if target > nums[-1]:
            return len(nums)
        i=0
        while(nums[i]<target):
            i+=1
            # if i>=len(nums):
            #     return i
        return i
# 二分查找
class Solution1:
    def searchInsert(self, nums: list, target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:return mid
            elif nums[mid] < target:
                # 避免整除导致的mid与left相同
                left = mid + 1
            else:
                # 避免right与left相同，但mid不等于target时陷入死循环
                right = mid -1
        return left

if __name__=="__main__":
    a=Solution1()
    print(a.searchInsert([1,3,5,6],2))