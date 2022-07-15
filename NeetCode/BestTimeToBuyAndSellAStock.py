def solution():
    # prices = [7, 6, 5, 4, 3, 2]
    # prices = [1, 2]
    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
    # prices = [1, 2, 4]
    # prices = [7, 1, 5, 3, 6, 4]
    # prices = [0, 1, 0, 2, 1]
    # prices = [2, 1, 2, 0, 1]
    # prices = [3, 2, 6, 5, 0, 3]
    # prices = [7, 5, 0, 0, 0, 0, 1, 5, 3, 6, 4, 1, 1, 1]
    start = 0
    results = []
    if len(prices) > 2:
        while start < len(prices) - 1:
            checker = start + 1
            while checker < len(prices):
                if prices[start] >= prices[checker]:
                    break
                else:
                    results.append(prices[checker] - prices[start])
                    checker += 1
            start += 1
    elif len(prices) == 2:
        if prices[0] < prices[1]:
            return prices[1] - prices[0]
    else:
        return 0
    if len(results) == 0:
        return 0
    return max(results)


print(solution())
