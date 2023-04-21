def maxProfit(prices):
    if len(prices) < 2:
        return 0
    l, r = 0, 1
    max_profit = 0
    while r < len(prices):
        profit = prices[r] - prices[l]
        if prices[r] <= prices[l]:
            l = r
        r += 1
        max_profit = max(max_profit, profit)
    return max_profit
