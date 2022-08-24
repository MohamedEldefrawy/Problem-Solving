import heapq


class KthLargest:
    # k = 0
    # nums = []

    # def __init__(self, k: int, nums: [int]):
    #     self.k = k
    #     self.nums = nums
    #     self.nums.sort(reverse=True)
    #
    # def add(self, val: int) -> int:
    #     if len(self.nums) < 3 :
    #         self.nums.append(val)
    #         self.nums.sort(reverse=True)
    #         return self.nums[self.k-1]
    #
    #     if self.nums[self.k - 1] > val:
    #         return self.nums[self.k - 1]
    #     else:
    #         self.nums.append(val)
    #         self.nums.sort(reverse=True)
    #         return self.nums[self.k - 1]
    def __init__(self, k: int, nums: [int]):
        self.k = k, self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
