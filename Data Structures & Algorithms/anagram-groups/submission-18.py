class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for i in strs:

            count = [0] * 26

            for c in i:
                count[ord(c) - ord("a")] += 1

            key = tuple(count)

            if key not in map:
                map[key] = []
            map[key].append(i)

        return list(map.values())
            