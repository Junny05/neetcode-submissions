class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        myset = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in myset:
                    dp[i] = True
                    break
        return dp[len(s)]
        