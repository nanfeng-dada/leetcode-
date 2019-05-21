# split()采用none为sep时，可以自动舍去末尾的空格
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        if len(l)==0:
            return 0
        return len(l[-1])

# 语言无差别解法
class Solution1:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt, tail = 0, len(s) - 1
        while tail >= 0 and s[tail] == ' ':
            tail -= 1
        while tail >= 0 and s[tail] != ' ':
            cnt += 1
            tail -= 1
        return cnt
if __name__=='__main__':

    a=Solution1()

    print(a.lengthOfLastWord('a fewigb    '))