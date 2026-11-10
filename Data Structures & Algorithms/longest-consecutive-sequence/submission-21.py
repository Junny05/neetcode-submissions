class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxlength = 0

        for num in nums:

            if num - 1 in nums:
                continue
                
            length = 1

            while num + length in nums:
                length += 1

            maxlength = max(length, maxlength)

        return maxlength