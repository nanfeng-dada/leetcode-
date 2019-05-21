# 这题比较简单，作差分，把大于零的涨幅加起来
class Solution:
    def maxProfit(self, prices: list) -> int:
        maxprofit=0
        for i in range(1,len(prices)):
            delta=prices[i]-prices[i-1]
            if delta>0:
                maxprofit+=delta
        return maxprofit