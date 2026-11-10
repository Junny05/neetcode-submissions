class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        curr = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            pre[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            post[i] = postfix
            postfix *= nums[i]

        for i in range(len(nums)):
            curr[i] = post[i] * pre[i]
        return curr