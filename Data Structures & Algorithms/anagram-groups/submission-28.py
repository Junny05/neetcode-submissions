class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            characters = [0] * 26
            for ch in s:
                index = ord(ch) - ord('a')
                characters[index] += 1                
            res[tuple(characters)].append(s)
        return list(res.values())