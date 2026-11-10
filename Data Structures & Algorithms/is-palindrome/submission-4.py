class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while (l < r):
            while l < r and s[l].lower() not in "abcdefghijklmnopqrstuvwxyz1234567890":
                l+=1
            while r > l and s[r].lower() not in "abcdefghijklmnopqrstuvwxyz1234567890":
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True