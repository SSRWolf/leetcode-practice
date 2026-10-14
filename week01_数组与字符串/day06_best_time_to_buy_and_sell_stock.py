"""LeetCode 121. 买卖股票的最佳时机

题目初始条件：给定每天的股价 prices，最多完成一次买入和一次卖出；卖出必须在买入之后。返回最大利润，无利润则返回 0。
样例输入：prices = [7, 1, 5, 3, 6, 4]
样例结果：5
请先独立完成；这里没有预填解法。
"""


class Solution:
    #1.暴力求解
    def maxProfit(self, prices: list[int]) -> int:
        # 在这里写你的解法
        
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit = prices[j]-prices[i]
                max_profit = max(profit,max_profit)

        return max_profit

    #2.单循环
    def maxProfit2(self, prices: list[int]) -> int:

        min_price = prices[0]
        max_profit = 0

        for price in prices:

            # 1. 假设今天卖出，计算利润
            profit = price-min_price

            # 2. 更新最大利润
            max_profit = max(profit,max_profit)

            # 3. 更新截至今天的最低价格
            min_price = min(min_price,price)            

        return max_profit
