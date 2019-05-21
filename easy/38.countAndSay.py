
# 先写递推函数，在循环调用
# 方法2可以将打印好的字符串存入字典，以空间换时间
class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s = self.getnext(s)
        return s

    def getnext(self,s):
        res = ''
        cnt = 1
        pre = s[0]
        for i in range(1, len(s)):
            if s[i] == pre:
                cnt += 1
            else:
                res = res + str(cnt) + pre
                pre = s[i]
                cnt = 1
        # 加上最后一个数
        res = res + str(cnt) + pre
        return res
if __name__=='__main__':
    a=Solution()
    print(a.countAndSay(5))