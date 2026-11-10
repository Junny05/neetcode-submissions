class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = [intervals[0]]
        removals = 0
        for start,end in intervals[1:]:
            if start < res[-1][1]:
                removals += 1
                res[-1][1] = min(res[-1][1], end)
            else:
                res.append([start,end])
        return removals
