class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


