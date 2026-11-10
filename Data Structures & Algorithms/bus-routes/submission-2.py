class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stop_to_bus = defaultdict(list)

        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_bus[stop].append(bus)
        
        q = deque(stop_to_bus[source])
        level = 1
        visited = set(stop_to_bus[source])

        while q:
            for _ in range(len(q)):
                bus = q.popleft()

                if target in routes[bus]:
                    return level
                
                for neighbors in routes[bus]: 
                    for bus in stop_to_bus[neighbors]:
                        if bus not in visited:
                            visited.add(bus)
                            q.append(bus)
            level += 1
        return -1

