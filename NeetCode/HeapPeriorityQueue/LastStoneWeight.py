import heapq

# stones = [2, 2]
# heapq.heapify(stones)
# stones.sort(reverse=True)
# while len(stones) > 1:
#     largest_stone = heapq.heappop(stones)
#     stones.sort(reverse=True)
#     second_largest = heapq.heappop(stones)
#     stones.sort(reverse=True)
#     if largest_stone != second_largest:
#         largest_stone -= second_largest
#         heapq.heappush(stones, largest_stone)
#         stones.sort(reverse=True)

stones = [2, 7, 4, 1, 8, 1]
stones = [-s for s in stones]
heapq.heapify(stones)

while len(stones) > 1:
    first_stone = heapq.heappop(stones)
    second_stone = heapq.heappop(stones)

    if second_stone > first_stone:
        heapq.heappush(stones, first_stone - second_stone)
stones.append(0)
print(stones[0])
