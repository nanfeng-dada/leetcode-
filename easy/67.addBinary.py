# 字符模拟二进制计算
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 1补齐长度
        # 2从尾部到头部模拟加法
        # 3进位处理、头部进位
        # 4输出切片
        d = abs(len(a) - len(b))
        if len(a) > len(b):
            b = '0' * d + b
        else:
            a = '0' * d + a
        l = len(a)
        s = ''
        up = 0
        for i in range(-1, -l - 1, -1):
            sums = int(a[i]) + int(b[i]) + up
            if sums >= 2:
                s = str(sums % 2) + s
                up = sums // 2
            else:
                s = str(sums) + s
                up = 0
        if up == 1:
            s = '1' + s
        return s
# pythonic做法
class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int('0b'+a,2)+int('0b'+b,2))[2:]

# 异或运算，不具备通用性
class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        flag = 0
        result = ''
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        for i in range(-1, -max_len - 1, -1):
            result = str(int(a[i]) ^ int(b[i]) ^ flag) + result
            if a[i] == '0' and b[i] == '0':
                flag = 0
            elif a[i] == '1' and b[i] == '1':
                flag = 1
        if flag == 1:
            result = '1' + result
        return result

if __name__=='__main__':

    a=Solution()

    print(a.addBinary('11110','101'))