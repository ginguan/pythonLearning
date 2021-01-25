#121. Best Time to Buy and Sell Stock
def maxProfit(self, prices):
    low = float('inf')
    profit = 0
    for i in prices:
        profit = max(profit, i-low)
        low = min(low, i)
    return profit

#122 Best Time to Buy and Sell Stock II

def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    profit = 0
    for i in range(1,len(prices)):
        if(prices[i]>prices[i-1]):
            profit += prices[i]-prices[i-1]
    return profit

#309. Best Time to Buy and Sell Stock with Cooldown

