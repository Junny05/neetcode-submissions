class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0

        stop_to_buses = defaultdict(list)

        # bus #1 : 1,2,7
        # bus #2 : 3,6,7
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].append(bus)
        
        # starting point would be 
        q = deque(stop_to_buses[source])
        level = 1
        visited = set(stop_to_buses[source])

        while q:

            for _ in range(len(q)):
                # get bus id
                busidx = q.popleft()

                # if target is in those routes of bus id
                if target in routes[busidx]:
                    return level

                # all the stops in that bus id
                for neighbor in routes[busidx]:
                    
                    # check bus in that route
                    for bus in stop_to_buses[neighbor]:

                        if bus not in visited:
                            q.append(bus)
                            visited.add(bus)
            level += 1
        return -1