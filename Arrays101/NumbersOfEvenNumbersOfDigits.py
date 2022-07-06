count = 0
nums = [12, 345, 2, 6, 7896]
for number in nums:
    if len(str(number)) % 2 == 0:
        count += 1
print(count)
