class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count ={}
        t_count ={}

        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)

        for i in range(len(t)):
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
        
        return t_count == s_count