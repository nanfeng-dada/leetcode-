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

if __name__=="__main__":
    a=Solution()
    print(a.searchInsert([1,3,5,6],5))