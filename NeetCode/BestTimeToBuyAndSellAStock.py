def solution():
    # prices = [7, 6, 5, 4, 3, 2]
    # prices = [1, 2]
    # prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
    # prices = [1, 2, 4]
    # prices = [7, 1, 5, 3, 6, 4]
    # prices = [0, 1, 0, 2, 1]
    # prices = [2, 1, 2, 0, 1]
    # prices = [3, 2, 6, 5, 0, 3]
    prices = [7, 5, 0, 0, 0, 0, 1, 5, 3, 6, 4, 1, 1, 1]
    buy = 0
    sell = 1
    profit = 0
    while sell < len(prices):
        if prices[buy] > prices[sell]:
            buy = sell
        else:
            profit = max(profit, prices[sell] - prices[buy])
        sell += 1
    return profit


print(solution())
