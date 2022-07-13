# nums = [1, 1]
# nums = [-3, -1, -1]
# nums = [-3, -1, -1, 0, 0, 2]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
index = len(nums) - 1
i = 0
k = 0

while i < index:
    j = i + 1
    while j <= index:
        while nums[i] == nums[j]:
            for l in range(j, index):
                nums[l] = nums[l + 1]
            nums[index] = -200
            index -= 1
            k += 1
        j += 1
    i += 1
print(nums)

print(k)
