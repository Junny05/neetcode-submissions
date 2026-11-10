class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(start, path):
            if sum(path) == target:
                res.append(path[:])
            if sum(path) > target:
                return

            for num in range(start, len(nums)):
                path.append(nums[num])
                dfs(num, path)
                path.pop()
            return res
        return dfs(0, path)