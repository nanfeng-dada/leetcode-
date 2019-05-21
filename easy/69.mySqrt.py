# 牛顿迭代，求解平方根，原理是做切线，求x轴交点作为下一次迭代点
# 初始条件x0只要不为零即可，因为0处切线斜率为0，终止条件本来是x/r与r差值小于求解精度
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r > x:
            r = (r + x/r) // 2
        return int(r)

#pythonic
class Solution1:
   def mySqrt(self, x: int) -> int:
       return int(x**0.5)

#二分查找超时
class Solution2:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        low=0
        up=x
        mid=(low+up)/2
        while (up>low):
            if mid>x/mid:
                up=mid
            elif mid<x/mid:
                low=mid
            else:
                return int(mid)
            mid=(up+low)/2



if __name__=='__main__':
    num=9
    a=Solution1()

    print(a.mySqrt(num))

    a = Solution2()
    print(a.mySqrt(num))