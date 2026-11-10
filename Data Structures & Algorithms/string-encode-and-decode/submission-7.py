class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string += i + ">"
        return string
        

    def decode(self, s: str) -> List[str]:
        arr = []
        empty = "" 
        for i in range(len(s)):
            if s[i] == ">":
                arr.append(empty)
                empty = ""
            else:
                empty += s[i]
        return arr
        
