class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        arr = []
        solution = []

        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i],0)
        
        for num,freq in map.items():
            arr.append([freq,num])
        arr.sort()

        while len(solution) < k:
            solution.append(arr.pop()[1])
        
        return solution
        

