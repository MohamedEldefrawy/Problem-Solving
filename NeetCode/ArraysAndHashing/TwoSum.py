nums = [2, 7, 11, 15]
target = 26


def sol():
    numbers_map = {}
    for i in range(len(nums)):
        if (target - nums[i]) in numbers_map.keys():
            return [numbers_map[target - nums[i]], i]
        else:
            numbers_map[nums[i]] = i


print(sol())