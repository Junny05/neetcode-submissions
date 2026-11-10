class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        array = []
        res = []
        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i],0)

        for j,l in map.items():
            array.append([l,j])
        
        array.sort()

        res = []
        while len(res) < k:
            res.append(array.pop()[1])
        return res
