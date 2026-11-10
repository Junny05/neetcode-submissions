class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for number in range(len(nums)):
            hashmap[nums[number]] = 1 + hashmap.get(nums[number], 0)

        sort = sorted(hashmap, key=lambda x: hashmap[x], reverse=True)

        return sort[:k]

