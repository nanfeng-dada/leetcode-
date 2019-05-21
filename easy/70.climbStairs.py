# 无备忘录的自顶向下动态规划不满足时间复杂度
class Solution:
    def climbStairs(self, n: int) -> int:
        # 初始化备忘录
        lst = [-1] * n
        lst[:3] = [1, 2, 3]
        return self.climbStairssub( n, lst)
    # 自顶下下设计，将求解n阶分解为求解n-1阶和n-2阶的和
    def climbStairssub(self, n, lst):
        if lst[n - 1] > 0:
            return lst[n - 1]
        if n <= 0:
            return 0
        else:
            lst[n - 1] = self.climbStairssub( n - 1, lst) + self.climbStairssub( n - 2, lst)
            return lst[n - 1]

# 自底向上设计，求解n阶前，现将小于n阶的情况求解出来
class Solution1:
    def climbStairs(self, n: int) -> int:
        lst=[-1]*n
        lst[:3]=[1,2,3]
        for i in range(3,n):
            lst[i]=lst[i-1]+lst[i-2]
        return lst[n-1]

# 自底向上设计，降低空间复杂度，
# 斐波那契数列方法
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        f1,f2=1,2
        for i in range(2,n):
            f1,f2=f2,f1+f2
        return f2
# logn时间复杂度解法，利用斐波那契公式
# 参见官方
# https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode/
# 不知道为什么精度有差

class Solution3:
    def climbStairs(self, n: int) -> int:
        sqrt5=5**0.5
        fn=(((1+sqrt5))/2)**(n+1)-(((1-sqrt5))/2)**(n+1)
        return int(fn/sqrt5)

if __name__=='__main__':
    num=100
    a=Solution()

    print(a.climbStairs(num))
    a=Solution1()

    print(a.climbStairs(num))
    a=Solution2()

    print(a.climbStairs(num))
    a=Solution3()

    print(a.climbStairs(num))