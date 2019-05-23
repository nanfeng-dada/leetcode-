# 与操作，判断尾部是否为1
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt=0
        while n:
            cnt+=n&1
            n>>=1
        return cnt
# 取余操作，判断尾部是否为1
class Solution1(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt=0
        while n:
            cnt+=n%2
            n>>=1
        return cnt
# n&n-1直接去除尾部的1
class Solution2(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt=0
        while n:
            cnt+=1
            n&=n-1
        return cnt
if __name__=='__main__':
    a=Solution1()

    print(a.hammingWeight(0b10101111))
    a=Solution2()

    print(a.hammingWeight(0b10101111))
    a=Solution()

    print(a.hammingWeight(0b10101111))