# mysolution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        l=len(haystack)
        l1=len(needle)
        for i in range(l-l1+1):
            if haystack[i:i+l1]==needle:
                return i
        return -1

# python骚操作
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)




if __name__=="__main__":
    a=Solution()
    print(a.strStr('a','a'))