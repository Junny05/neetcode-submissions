class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        res = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            map[sorted_s].append(s)
        
        for value in map.values():
            res.append(value)

        return res