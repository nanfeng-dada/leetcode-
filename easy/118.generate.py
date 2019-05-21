# 循环
class Solution:
    def generate(self, numRows: int) -> list:
        # 题意: 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
        # 思路: 模拟
        # 第一行有一个数，第n行有n个数

        res = []
        for i in range(numRows):
            tmp = [1]*(i+1)
            if i >= 2:
                for j in range(1, i):
                    tmp[j] = res[i-1][j] + res[i-1][j-1]
            res.append(tmp)
        return res

# 递归的方法
class Solution1:
    def generate(self, numRows: int) -> list:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            out = [[1], [1, 1]]
            for i in range(2, numRows):
                out.append(self.getnext(out[i - 1]))
            return out

    def getnext(self, lst):
        l = len(lst)
        lstn = []
        for i in range(l - 1):
            lstn.append(lst[i] + lst[i + 1])
        return [1] + lstn + [1]