class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            character = [0] * 26
            for letter in word:
                character[ord(letter) - ord('a')] += 1
            if tuple(character) not in res:
                res[tuple(character)] = []
            res[tuple(character)].append(word)
        return list(res.values())