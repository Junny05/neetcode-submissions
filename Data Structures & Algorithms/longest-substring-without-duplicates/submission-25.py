class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        maxlength = 0
        
        for i in range(len(s)):
            print(res)
            if s[i] not in res:
                res.append(s[i])
            else:
                while s[i] in res:
                    res.remove(res[0]) 
                res.append(s[i])
            maxlength = max(len(res), maxlength)
        return maxlength