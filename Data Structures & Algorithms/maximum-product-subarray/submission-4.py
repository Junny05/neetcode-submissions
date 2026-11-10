class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        currmax = nums[0]
        currmin = nums[0]
        res = nums[0]
        for i in range(1,(len(nums))):
            temp = currmax
            currmax = max(nums[i], currmax * nums[i], currmin * nums[i])
            currmin = min(nums[i], temp * nums[i], currmin * nums[i])
            res = max(currmax, res)
        return res