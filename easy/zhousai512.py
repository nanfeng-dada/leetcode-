
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #xy角度
        status=[[0,0,90]]
        for s in instructions:
            st = status[-1].copy()
            if s=='G':
#                 判断前方是什么方向
                if status[-1][2]==90:
                    st[1]+=1

                elif status[-1][2]==0:
                    st[0]+=1

                elif status[-1][2]==270:
                    st[1]-=1

                elif status[-1][2]==180:
                    st[0]-=1
                status.append(st)
            elif s=='L':
                st[2]-=90
                if st[2]>=360:
                    st[2]=st[2]-360
                elif st[2]<0:
                    st[2] = st[2] +360
                status.append(st)
            elif s=='R':
                st[2]+=90
                if st[2]>=360:
                    st[2]=st[2]-360
                elif st[2]<0:
                    st[2] = st[2] +360
                status.append(st)



        for i in status:
            print(i)
        if status[-1]==status[0]:
            return True
        else:
            return False
class Solution1(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # i,j为坐标，d为方向，k为单个命令中的索引
        vis = set()
        i = j = 0
        ds = ((0,1),(1,0),(0,-1),(-1,0))
        d = 0
        for _ in range(100):
            for k, s in enumerate(instructions):
                if (i,j,d,k) not in vis:
                    vis.add((i, j, d, k))
                    if s == 'G':
                        di, dj = ds[d]
                        i += di
                        j += dj
                    elif s == 'L':
                        d += 1
                        d %= 4
                    else:
                        d -= 1
                        if d < 0:
                            d += 4
                        d %= 4
                else:
                    return True
        return False
if __name__=='__main__':

    a=Solution1()
    print(a.isRobotBounded('GGLLGG'))
