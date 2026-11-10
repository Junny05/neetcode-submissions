class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i], 0)
        
        for j in map.values():
            if j >= 2:
                return True
        return False