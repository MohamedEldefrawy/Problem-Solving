nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
left = right = 1
while right < len(nums):
    if nums[right] != nums[right - 1]:
        nums[left] = nums[right]
        left += 1
    right += 1

print(nums)
print(left)
