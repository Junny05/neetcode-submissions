class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def dp(steps):
            if steps == 1: return 1
            if steps == 2: return 2


            if steps in memo: 
                return memo[steps]

            memo[steps] = dp(steps-1) + dp(steps-2)

            return memo[steps]

        return dp(n)