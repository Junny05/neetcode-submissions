class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        if len(stones) == 1:
            return stones[0]
        #7 - 3 = 4
        # 4 - -2 = 6
        for stone in stones:
            heapq.heappush(heap, -stone)

        while heap:
            if len(heap) >= 2:
                stone1 = heapq.heappop(heap)
                stone2 = heapq.heappop(heap)
                if stone1 == stone2:
                    continue
                if stone2 > stone1:
                    heapq.heappush(heap, stone1-stone2)
            else:
                return abs(heap[0])
        return 0