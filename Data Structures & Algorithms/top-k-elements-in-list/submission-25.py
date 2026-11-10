class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        array = []
        res = []
        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i],0)

        for j,l in map.items():
            array.append([j,l])
        
        array.sort(key=lambda x:x[1])

        res = array[-k:]

        return [num for num, fres in res]