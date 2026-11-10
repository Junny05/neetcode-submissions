class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_buses = defaultdict(list)

        for bus_num, stops in enumerate(routes):     
            for stop in stops:
                stop_to_buses[stop].append(bus_num)
        
        q = deque(stop_to_buses[source])
        visited = set(stop_to_buses[source])
        level = 1
        while q:
            for _ in range(len(q)):
                curr_bus = q.popleft()

                if target in routes[curr_bus]:
                    return level

                for neighbor in routes[curr_bus]:
                    for bus in stop_to_buses[neighbor]:
                        if bus not in visited:
                            q.append(bus)
                            visited.add(bus)
            level += 1
        return -1