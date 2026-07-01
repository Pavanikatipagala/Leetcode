class Solution(object):
    def maxProfit(self, prices):
        mini=prices[0]
        best_profit=0
        for i in range(len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            t_profit=prices[i]-mini
            if t_profit >best_profit:
                best_profit=t_profit
        return best_profit

        