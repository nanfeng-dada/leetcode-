class Solution:
    def convertToTitle(self, n: int) -> str:
        #         Z,A,B.......X,Y
        # 相当于10进制中的0,1,2.....9
        lst = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        s = ''

        while n:
            #             精辟的一句，把A-Z映射为0-25
            n -= 1
            s = lst[n % 26] + s
            n = n // 26
        return s

if __name__=="__main__":
    a=Solution()
    print(a.convertToTitle(26))