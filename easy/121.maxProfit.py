# 动态规划，第i天的最大收益=max（第i-1天的最大收益，第i天的价格-前i-1天历史最低价格）
class Solution:
    def maxProfit(self, prices: list) -> int:
        maxprofit = 0
        minprice = 1 << 31
        for i in range(1, len(prices)):
            minprice = min(minprice, prices[i - 1])
            maxprofit = max(maxprofit, prices[i] - minprice)
        return maxprofit
if __name__=='__main__':
    a=Solution()
    print(a.maxProfit([7,5,6,7,4,8,5]))
