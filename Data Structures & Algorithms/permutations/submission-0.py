class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        # 2 ^ 6 
        def backtracking(path):
            if len(path) == len(nums):
                sol.append(path[:])
            
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtracking(path)
                    path.pop()
        
        backtracking([])
        return sol
        