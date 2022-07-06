def solve():
    # nums1 = [1, 2, 3, 0, 0, 0]
    nums1 = [0]
    # m = 3
    m = 0
    # nums2 = [2, 5, 6]
    nums2 = [1]
    # n = 3
    n = 1
    for number in nums2:
        nums1[m] = number
        m += 1
    return nums1.sort()


solve()
