class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for a,b in intervals:

            if b < newInterval[0]:
                res.append([a,b])
            elif a > newInterval[1]:
                res.append([newInterval[0],newInterval[1]])
                newInterval = [a,b]
            else:            
                newInterval = [min(a,newInterval[0]),max(b,newInterval[1])]
        res.append(newInterval)
        return res