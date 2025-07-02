class Solution:
    def maximumProfit(self, prices):
        profit = 0
        mini = prices[0]
        for i in range(1, len(prices)):
            mini = min(mini, prices[i])  
            cost = prices[i] - mini      
            profit = max(profit, cost)  
        return profit
