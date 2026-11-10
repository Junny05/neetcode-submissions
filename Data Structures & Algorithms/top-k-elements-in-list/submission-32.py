class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        arr = []
        res = []

        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i],0)
        
        for num,freq in map.items():
            arr.append([freq,num])
        
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        

