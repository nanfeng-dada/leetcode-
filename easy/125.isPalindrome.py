# pythonic做法，正则表达式去除指定字符
import re
class Solution:

    def isPalindrome(self, s: str) -> bool:
        r='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ]+'
        s=re.sub(r,'',s).lower()
        l=len(s)
        mid = l >> 1
        if l%2:

            return s[:mid] == s[mid + 1:][::-1]
        else:
            return s[:mid] == s[mid :][::-1]

# 无语言差别做法

class Solution1:
    def isPalindrome(self, s: str) -> bool:

        l = len(s)
        if l == 0:
            return True
        left = 0
        right = l - 1
        while right > left:
            while (right > left and not s[left].isalnum()):
                left += 1
            while (right > left and not s[right].isalnum()):
                right -= 1
            if (s[left].lower() != s[right].lower()):
                return False
            else:
                left += 1
                right -= 1

        return True
if __name__=='__main__':
    a=Solution1()
    print(a.isPalindrome("!!!"))