class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = []

        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i-1]):
                continue

            l = i + 1
            r = len(nums) - 1
            while(l < r):
                target = -nums[i]
                if (nums[l] + nums[r] < target):
                    l+=1
                elif (nums[l] + nums[r] > target):
                    r-=1
                else:
                    lst.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return lst