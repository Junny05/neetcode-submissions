class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # manhattan distance between two units
        # from first point to next closest point then next closest point add up cost
        # prob BFS with a helper function with distance calculation 
        # BFS with WEIGHTS (from distance calculation)

        def calculate(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        # cost
        cost = 0

        # distance, index of points
        heap = [(0, 0)]

        # marking it as visited
        visited = set()

        while heap:
            distance, index = heapq.heappop(heap)
            
            if index in visited:
                continue
            else:
                visited.add(index)
                cost += distance

            if len(visited) >= len(points):
                return cost

            for i in range(len(points)):
                if i not in visited:
                    heapq.heappush(heap, (calculate(points[index],points[i]),i))
        return cost





