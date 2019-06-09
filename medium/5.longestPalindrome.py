# 动态规划
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        maxl=1
        start=0
        l=len(s)
        dp=[[False]*l for _ in range(l)]
        # init dp
        for i in range(l):
            dp[i][i]=True
            if i+1<l and s[i]==s[i+1]:
                dp[i][i+1]=True
                maxl=2
                start=i



        for ls in range(3,l+1):
            for i in range(l-ls+1):
                j=i+ls-1

                dp[i][j] =  dp[i+1][j-1] and s[i]==s[j]
                print(s[i:j+1],dp[i][j])

                if dp[i][j] and j-i+1>maxl:
                    maxl=j-i+1
                    start=i

        return s[start:start+maxl]
# dp精炼版
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s :
            return ""
        res = ""
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = float("-inf")
        #print(dp)
        for i in range(n):
            for j in range(i,-1,-1):
                if s[i] == s[j] and (i - j < 2 or dp[i-1][j+1]):
                    dp[i][j] = 1
                if dp[i][j] and  max_len < i - j + 1:
                    #print("i,j",i,j)
                    res = s[j:i+1]
                    max_len = i - j + 1
        return res
# 非马拉车on算法
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s
        maxLen = 0
        for i in range(len(s)):
            if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
                maxLen += 2
                end = i
                continue
            if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                maxLen += 1
                end=i
        return s[end-maxLen+1:end+1]