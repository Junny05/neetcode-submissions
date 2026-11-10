class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        sum = int(len(nums) * (len(nums)+1) /2)
    
        for i in range(len(nums)):
            sum = sum - nums[i]
        return sum