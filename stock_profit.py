def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    
    return max_profit



prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))   