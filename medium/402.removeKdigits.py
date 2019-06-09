# 都说是贪心算法，但是感觉是找规律找出来的
# 从前到后依次遍历，找到第一个非递增的数字的前一个，删去
# 如果全为递增，则删除最后一个（非严格递增）
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        lens = len(num)
        j = 0

        if (k >= lens):
            return '0'

        stack = list(num)

        for _ in range(k):
            while (j < len(stack) - 1 and stack[j] <= stack[j + 1]):
                j += 1
            stack.pop(j)
            j = max(0, j - 1)
        result = ''.join(stack).lstrip('0')
        return result if result else '0'
