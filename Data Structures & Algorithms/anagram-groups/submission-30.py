class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            characters = [0] * 26
            for chara in word:
                index = ord(chara) - ord('a')
                characters[index] += 1
            res[tuple(characters)].append(word)
        return list(res.values())
            
