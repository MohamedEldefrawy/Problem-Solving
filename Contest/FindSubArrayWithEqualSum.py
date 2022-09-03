# Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.
#
# Return true if these subarrays exist, and false otherwise.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
nums = [1, 2, 3, 1, 0, 2]


def findSubarrays():
    numbers_map = {}
    for i in range(len(nums) - 1):
        if (nums[i] + nums[i + 1]) in numbers_map.keys():
            return True
        else:
            numbers_map[nums[i] + nums[i + 1]] = i
    return False


print(findSubarrays())
