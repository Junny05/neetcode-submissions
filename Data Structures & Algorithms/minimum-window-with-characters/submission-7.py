class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        s_count = {}
        t_count = {}

        for i in range(len(t)):
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
        have,need = 0, len(t_count)
        res, maxres = "", float("inf")
        l = 0

        for r in range(len(s)):
            s_count[s[r]] = 1 + s_count.get(s[r], 0)
            if s[r] in t_count and t_count[s[r]] == s_count[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < maxres:
                    maxres = r - l + 1
                    res = s[l:r+1]
                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        return res

                