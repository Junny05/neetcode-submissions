class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] curr length of subsequence 
        # for every value, false or true if true count +=1

        if len(nums) == 1:
            return 1

        dp = [1] * len(nums)
        dp[0] = 1

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)