cost = [10, 15, 20]
cost.append(0)
for i in range(len(cost) - 3,-1,-1):
    cost[i] += min(cost[i + 1], cost[i + 2])

print(min(cost[0], cost[1]))

