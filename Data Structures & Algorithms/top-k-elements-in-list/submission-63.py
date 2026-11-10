class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        res = []
        arr = []

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        
        for num, freq in count.items():
            arr.append([freq, num])
        
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
        return res