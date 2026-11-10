class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        longest = 0
        for n in myset:
            if n-1 not in myset:
                length = 1
                while n+length in myset:
                    length += 1
                longest = max(length, longest)
        return longest