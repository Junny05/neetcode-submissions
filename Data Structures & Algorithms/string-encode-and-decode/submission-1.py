class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in range(len(strs)):
            string += str(len(strs[i])) + "#" + strs[i]
        return string

    def decode(self, s: str) -> List[str]:
        lst = []
        left = 0

        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            length = int(s[left:right])
            left = right + 1
            right = left + length
            lst.append(s[left:right])
            left = right

        return lst
