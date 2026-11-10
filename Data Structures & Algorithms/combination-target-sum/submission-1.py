class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        visited = set()
        def dfs(start, path):
            nonlocal res
            if sum(path) == target:
                res.append(path[:])
                return
            
            if sum(path) > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i, path)
                path.pop()
            return res
        
        return dfs(0, [])
