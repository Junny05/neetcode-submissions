class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        myset = set(nums)
        n = len(nums)

        for i in range(n):
            if i not in myset:
                return i
        return n
        