class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        maps = {}

        for i in nums:
            maps[i] = 1 + maps.get(i,0)
        
        for j,k in maps.items():
            if k == 1:
                return j