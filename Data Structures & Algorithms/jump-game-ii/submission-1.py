class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, currEnd, maxReach = 0,0,0

        for i in range(len(nums)-1):
            maxReach = max(maxReach, i + nums[i])
            if i == currEnd:
                jumps+=1
                currEnd = maxReach
        return jumps