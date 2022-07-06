results = []
nums = list(map(int, input().split()))
sum = 0
for number in nums:
    sum += number
    if number == 0:
        sum = 0
    results.append(sum)

print(max(results))
