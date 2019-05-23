class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s=bin(n)[2:]
        s='0'*(32-len(s))+s
        s=s[::-1]
        num=int(s,2)
        return num
# 上述代码精简版：
class Solution1:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], base=2)


class Solution2:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        count = 32

        while count:
            res <<= 1
            # 取出 n 的最低位数加到 res 中
            res += n & 1
            n >>= 1
            count -= 1

        return int(bin(res), 2)
if __name__=='__main__':
    a=Solution2()

    print(a.reverseBits(0b10101111))
    a = Solution1()

    print(a.reverseBits(0b10101111))