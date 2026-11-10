class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i],0) + 1
        
        for value in map.values():
            if value >= 2:
                return True
        return False