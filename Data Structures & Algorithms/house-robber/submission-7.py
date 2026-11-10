class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dp(i):
            if i >= len(nums):
                return 0

            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(nums[i] + dp(i + 2), dp(i+1))

            return memo[i]

        return dp(0)
