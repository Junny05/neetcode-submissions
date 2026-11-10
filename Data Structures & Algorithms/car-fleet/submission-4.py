class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)

        times = []
        count = 0
        ahead = 0

        for position, speed in pairs:
            times.append((target-position) / speed)
        
        for i in range(len(times)):
            if times[i] > ahead:
                count +=1
                ahead = max(ahead, times[i])

        return count

        
        