# dp来做，稍微给这个公式变形成A[i]+i+A[j]-j，这样就可以看成是左A[i]+i和右A[j]-j两部分和的最大值。
# 随着遍历数组，我们对两部分和取最大值，并且若当前的值—下标对之和比之前更大，我们就更新left部分的值即可。
# j》i，因此j从1开始，A[i]+i的最大化需在A[i]+i+A[j]-j最大化后进行
class Solution:
    def maxScoreSightseeingPair(self, A: list) -> int:
        left, res = A[0], -1
        for j in range(1, len(A)):
            res = max(res, left + A[j] - j)
            left = max(left, A[j] + j)
        return res

class Solution1:
    def maxScoreSightseeingPair(self, A: list) -> int:
        cur = res = 0
        for a in A:
            res = max(res, cur + a)
            cur = max(cur, a) - 1
        return res
if __name__=='__main__':
    a=Solution()
    print(a.maxScoreSightseeingPair([8,1,5,2,6]))
    a=Solution1()
    print(a.maxScoreSightseeingPair([8,1,5,2,6]))