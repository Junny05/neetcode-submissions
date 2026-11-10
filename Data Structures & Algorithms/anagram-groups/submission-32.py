class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # act: "a": 1, "c": 1, "t": 1
        res = defaultdict(list)
        for word in strs:
            character = [0] * 26
            for chara in word:
                index = ord(chara) - ord('a')
                character[index] += 1
            res[tuple(character)].append(word)
        return list(res.values())