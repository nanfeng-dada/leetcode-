class Solution:
    def search(self, nums: list, target: int) -> bool:
        n = len(nums)
        if n == 0:
            return False
        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        #print(left,right)
        return nums[left] == target
if __name__=="__main__":
    a=Solution()
    print(a.search([1,3,1,1,1],3))