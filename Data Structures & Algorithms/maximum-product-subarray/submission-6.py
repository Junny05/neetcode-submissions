class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [1] * len(nums)
        # [1,1,1,1]
        # [2,1,1,1]
        # []
        dp[0] = nums[0]
        currMin = nums[0]
        currMax = nums[0]
        OverallMax = nums[0]
        for i in range(1,len(nums)):
            temp = currMin
            currMin = min(nums[i], nums[i] * currMin,nums[i]*currMax)
            currMax = max(nums[i], nums[i] * currMax, temp*nums[i])
            OverallMax = max(currMin,currMax,OverallMax)
        res = max(OverallMax, currMin,currMax)
        return res