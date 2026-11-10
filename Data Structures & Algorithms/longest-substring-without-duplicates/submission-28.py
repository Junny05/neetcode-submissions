class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # zxyzxyz
        
        maxlength = 0
        seen = set()
        l = 0
        
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
                seen.add(s[r])
            maxlength = max(maxlength, r - l + 1)
        return maxlength
        