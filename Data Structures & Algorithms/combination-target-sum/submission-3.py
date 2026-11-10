class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(start, path):

            # if sum of the path is equal to target then add to result
            if sum(path) == target:
                res.append(path[:])
                return

            # if greater then nothing
            if sum(path) > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i,path)
                path.pop()
            
        dfs(0,[])
        return res
