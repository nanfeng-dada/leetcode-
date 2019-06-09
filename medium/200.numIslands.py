import copy
class Solution:
    # global pos,cnt,m,n
    # pos = []
    # cnt = 0
    # m,n=0,0
    # 上面这种写法出错，由于创建类之后，多次调用方法numIslands，但是每次cnt却按照上一次的值更新
    # 正确的做法应该是把全局变量的创建放在方法中
    def numIslands(self, grid: list) -> int:
        gridtmp=copy.deepcopy(grid)
        def dfs(gridtmp,i, j):
            m, n = len(gridtmp), len(gridtmp[0])
            # 将return写在递归代码开头，及时返回，避免产生多个递归分支
            if i<0 or j<0 or i>=m or j>=n or gridtmp[i][j]!='1':
                return
            else:
                gridtmp[i][j]='0'
                dfs(gridtmp,i-1, j)
                dfs(gridtmp,i, j-1)
                dfs(gridtmp,i+1, j)
                dfs(gridtmp,i, j+1)

        # global cnt,m,n
        cnt=0
        if not gridtmp or not gridtmp[0]:
            return 0
        m, n = len(gridtmp), len(gridtmp[0])


        for i in range(m):
            for j in range(n):
                if gridtmp[i][j]=='1':
                    dfs(gridtmp,i,j)
                    cnt+=1
        return cnt


class Solution1:
    def numIslands(self, grid: list) -> int:
        try:
            m = len(grid)
            n = len(grid[0])
        except:
            return 0

        # -------------------------DFS 开始------------------------
        # 定义dfs递归方程
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and int(grid[i][j]):
                grid[i][j] = '0'
                for a, b in ((1, 0), (0, -1), (-1, 0), (0, 1)):
                    dfs(i + a, j + b)

        # ---------------------------------------------------------

        r = 0
        for i in range(m):
            for j in range(n):
                r += int(grid[i][j])
                dfs(i, j)  # 调用dfs沉没一整块陆地
        return r




if __name__=="__main__":
    grid=[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

    # a=Solution1()
    # print(a.numIslands(grid))
    a=Solution()
    print(a.numIslands(grid))
    print(a.numIslands(grid))