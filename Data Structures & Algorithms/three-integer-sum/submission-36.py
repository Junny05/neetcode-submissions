class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-1):
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while (r > l):
                if nums[l] + nums[r] > target:
                    r -=1
                elif nums[l] + nums[r] < target:
                    l +=1
                else:
                    res.append([nums[l],nums[i],nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    r-=1
        return res



                    