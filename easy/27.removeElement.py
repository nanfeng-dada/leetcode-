# 在python中复制操作重新赋一个标识符,所以可以直接赋值
class Solution():
    def removeElement(self, nums: list, val: int) -> int:
        lst=[]
        for i in range(len(nums)):
             if nums[i]!=val:
                    lst.append(nums[i])
        nums[:]=lst
        return len(lst)

#python计数与删除操作
class Solution2:
    def removeElement(self, nums, val):
        c = nums.count(val)
        i = 0
        while i < c:
            nums.remove(val)
            i += 1
        return len(nums)
# 正常解法为快慢指针
class Solution1():
    def removeElement(self, nums: list, val: int) -> int:
        cur_next=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[cur_next]=nums[j]
                cur_next+=1

        return cur_next
# 上面的解法的另一种书写形式
class Solution4:
    def removeElement(self, nums: list, val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums[i] = nums[-1]
                del nums[-1]
            else:
                i += 1
        return len(nums)
if __name__=="__main__":
    a=Solution1()
    print(a.removeElement([3,2,2,3],3))