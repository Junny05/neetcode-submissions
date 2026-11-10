class MedianFinder:
    def __init__(self):
        self.lower, self.upper = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)
        if self.lower and self.upper and (-self.lower[0] > self.upper[0]):
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        if len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        elif len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if (len(self.lower) + len(self.upper)) % 2 == 0:
            return (-self.lower[0] + self.upper[0]) / 2
        else:
            if len(self.lower) > len(self.upper):
                return -self.lower[0]
            elif len(self.lower) < len(self.upper):
                return self.upper[0]
    