"""coding: utf-8"""
# python字符切片操作,注意用切片方式剔除-号很费时间，
# tmp = -int(str(x)[::-1])   56 ms	13 MB
# tmp=-int(str(x)[1:][::-1])   64 ms	13.1 MB
class Solution:
    def reverse(self, x: int) -> int:

        if x<0:
            x=-x
            tmp = -int(str(x)[::-1])
            # tmp=-int(str(x)[1:][::-1])
        else:
            tmp=int(str(x)[::-1])
        if tmp > 2 ** 31 - 1 or tmp < -2 ** 31:
            return 0
        else:
            return tmp

#整除，求余方法取出每个数位的数字
# 56 ms	12.9 MB
class Solution1:
    def reverse(self, x: 'int') -> 'int':
        res = 0
        flag = False
        if x < 0:
            flag = True
            x = -x
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10
            if res > 2**31-1 or res < -2**31:
                return 0
        if flag:
            res = -res
        return res


if __name__=='__main__':

    a=Solution()

    print(a.reverse(1534236469))