class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1:1, 2:2, 3:3
        # while i < k: (2) 
        # add one to i
        # pop freq, value from nums, append to result
        freq = {}
        res = []

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        arr = []
        for key, freqs in freq.items():
            arr.append([freqs, key])
        
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
        return res
