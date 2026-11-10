class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i 
        for j in range(len(nums)):
            difference = target - nums[j]
            print(map)
            if difference in map.keys() and map.get(difference) != j:
                return [j,map.get(difference)]