class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        maxlen = 0

        left = 0

        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])
            maxlen = max(maxlen, len(hashset))
        return maxlen