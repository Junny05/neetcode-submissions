class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # k sized sliding sum, we want max of each k-sized sliding to be appended to max
        # we want to return amx which has max of each of the k-sized sliding window
        # L --> R we can check using r - l + 1
        # nums[l+1:r] l = 0 r = 
        # 
        l = 0
        res = []
        if len(nums) == 1:
            return [nums[0]]

        # 1,2,1,0,4,2,6
        # L R
        for r in range(len(nums)):
            print(l,r)
            if r - l + 1 > k:
                l += 1
            if r - l + 1 == k:
                res.append(max(nums[l:r+1]))
        return res
            
            