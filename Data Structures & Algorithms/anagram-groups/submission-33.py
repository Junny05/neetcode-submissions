class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            character = [0] * 26
            for s in word:
                index = ord(s) - ord('a')
                character[index] += 1
            res[tuple(character)].append(word)
        return list(res.values())