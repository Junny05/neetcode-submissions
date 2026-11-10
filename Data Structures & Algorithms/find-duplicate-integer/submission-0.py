class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        new_set = set()

        for i in range(len(nums)):
            if nums[i] not in new_set:
                new_set.add(nums[i])
            else:
                return nums[i]
        return None
        