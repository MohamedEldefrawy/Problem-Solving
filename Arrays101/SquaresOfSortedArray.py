import math

nums = [-4, -1, 0, 3, 10]
result = []
for number in nums:
    result.append(int(math.pow(number, 2)))
print(sorted(result))
