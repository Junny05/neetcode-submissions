class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string += i + "<"
        return string

    def decode(self, s: str) -> List[str]:
        arr = []
        bucket = ""
        for i in range(len(s)):
            if s[i] != "<":
                bucket += s[i]
            else:
                arr.append(bucket)
                bucket = ""
        return arr
        
