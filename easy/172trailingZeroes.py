class Solution:
    def trailingZeroes(self, n: int) -> int:
        num=2
        for i in range(3,n+1):
            num=num*i
        return num
if __name__=="__main__":
    a=Solution()
    print(a.trailingZeroes(40))
