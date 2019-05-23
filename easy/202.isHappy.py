
# 按照快乐数的定义做就是了
# 还有一种找到了不快乐数的循环，这种非一般的解法不做考虑，机试的时候一般想不到
class Solution:
    def isHappy(self, n: int) -> bool:
        for _ in range(100):
            n1 = 0
            while n:
                n1 += (n % 10) ** 2
                n //= 10
            if n1 == 1:
                return True
            n = n1
        return False

# 保存一下结果，加速
class Solution1(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        already = set()

        while n != 1:
            num = 0
            while n > 0:
                tmp = n % 10
                num += tmp ** 2
                n //= 10

            if num in already:
                return False
            else:
                already.add(num)

            n = num

        return True
    