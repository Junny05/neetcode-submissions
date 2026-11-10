class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for s in strs:
            char = [0] * 26

            for stri in s:

                char[ord(stri) - ord('a')] += 1
            
            key = tuple(char)

            if key not in map:
                map[key] = []
            map[key].append(s)
        return list(map.values())
