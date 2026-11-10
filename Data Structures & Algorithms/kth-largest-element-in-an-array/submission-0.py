class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        count = 0

        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])

        while count != k:
            res = heapq.heappop(heap)
            count += 1
        return -res
        