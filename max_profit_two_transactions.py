def max_profit_two_transactions(prices):
    n = len(prices)
    
    if n == 0:
        return 0

    
    profit = [0] * n

    
    max_price = prices[n - 1]
    for i in range(n - 2, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        profit[i] = max(profit[i + 1], max_price - prices[i])

   
    min_price = prices[0]
    for i in range(1, n):
        if prices[i] < min_price:
            min_price = prices[i]
        profit[i] = max(profit[i - 1], profit[i] + (prices[i] - min_price))

    return profit[n - 1]



prices = [10, 22, 5, 75, 65, 80]
print("Maximum Profit:", max_profit_two_transactions(prices))