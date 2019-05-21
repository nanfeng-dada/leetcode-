# 在generate的基础上修改
class Solution:
    def getRow(self, rowIndex: int) -> list:

        res = []
        for i in range(rowIndex + 1):
            tmp = [1] * (i + 1)
            if i >= 2:
                for j in range(1, i):
                    tmp[j] = res[i - 1][j] + res[i - 1][j - 1]
            res.append(tmp)
        return tmp

# 采用两个一维列表减小空间复杂度
class Solution1:
    def getRow(self, rowIndex: int) -> list:

        res = []
        for i in range(rowIndex + 1):
            tmp = [1] * (i + 1)
            if i >= 2:
                for j in range(1, i):
                    tmp[j] = res[j] + res[j - 1]
            res = tmp
        return tmp
# 递归思路
class Solution2:
    def getRow(self, numRows: int) -> list:

        if numRows == 0:
            return [1]
        elif numRows == 1:
            return [1, 1]
        else:
            out=[1, 1]
            for i in range(2, numRows+1):
                out=self.getnext(out)
            return out

    def getnext(self, lst):
        l = len(lst)
        lstn = []
        for i in range(l - 1):
            lstn.append(lst[i] + lst[i + 1])
        return [1] + lstn + [1]