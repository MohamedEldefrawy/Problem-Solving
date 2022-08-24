nums = [-1, 0, 3, 5, 9, 12]
target = 9


def search():
    left = 0
    right = len(nums) - 1
    mid = int((left + right) / 2)

    while left <= right:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
            mid = int((left + right) / 2)
        else:
            right = mid - 1
            mid = int((left + right) / 2)
    return -1


print(search())
