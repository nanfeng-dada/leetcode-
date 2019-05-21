"""coding: utf-8"""
#切片
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False



if __name__=='__main__':
    a=Solution()
    print(a.isPalindrome(12421))