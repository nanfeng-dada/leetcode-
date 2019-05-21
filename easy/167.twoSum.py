# 双指针利用数组有序
class Solution:
    def twoSum(self, numbers: list, target: int):
        if len(numbers) <= 1:
            return None
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1


if __name__=="__main__":
    a=Solution()
    print(a.twoSum([2,7,11,15],9))