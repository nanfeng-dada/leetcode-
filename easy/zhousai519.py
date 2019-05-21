# 第一题
class Solution:
    def lastStoneWeight(self, stones: list) -> int:
        stones.sort()

        while len(stones)>2:
            sstone=self.fensui(stones[-2],stones[-1])
            if sstone:
                idx=0
                stones = stones[:len(stones) - 2]
                while idx<len(stones) and sstone>stones[idx]:
                    idx+=1
                stones=stones[:idx]+[sstone]+stones[idx:]
            else:
                stones = stones[:len(stones)-2]
        if len(stones)==1:
            return stones[0]
        else:
            return self.fensui(stones[-2],stones[-1])

    def fensui(self,x,y):
        if x==y:
            return 0
        else:
            return y-x
#  第二题
class Solution1:
    def removeDuplicates(self, S: str) -> str:
        self.unique = False

        while not self.unique:
            S=self.delonce(S)
        return S


    def delonce(self, s):
        l=len(s)
        if l<2:
            self.unique = True
            return s
        elif l==2:
            if s[-1]!=s[-2]:
                self.unique = True
                return s
            else:
                return s[0]
        news = ''
        pre=s[0]
        cnt=1
        for i in range(1,l):
            if pre==s[i]:
                cnt+=1

            else:
                if cnt%2:
                    news+=pre
                cnt = 1
            pre = s[i]

        if s[-1]!=s[-2]:
            news+=s[-1]
        elif cnt % 2:


            news += s[-1]




        if s==news:
            self.unique=True
        return news
if __name__=='__main__':
    # a=Solution()
    # print(a.lastStoneWeight([3,7,2]))
    a=Solution1()
    # print(a.removeDuplicates('abbbaca'))
    print(a.removeDuplicates('abbaca'))