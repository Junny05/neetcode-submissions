class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [1] * len(nums)
        postfix_array = [1] * len(nums)
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            prefix_array[i] = prefix 
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            postfix_array[i] = postfix
            postfix *= nums[i]

        for i in range(len(nums)):
            res[i] = prefix_array[i] * postfix_array[i]

        return res