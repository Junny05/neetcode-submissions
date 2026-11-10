class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        q = deque()
        heap = []
        time = 0

        for t in tasks:
            count[t] = count.get(t,0) + 1
        
        for freq in count.values():
            heapq.heappush(heap, -freq)
        
        while heap or q:
            time += 1

            if heap:

                count = heapq.heappop(heap) + 1

                if count != 0:
                    q.append((count, time + n))
            
            if q and q[0][1] <= time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time
        