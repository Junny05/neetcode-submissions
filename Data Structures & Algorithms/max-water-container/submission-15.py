class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxwater = 0

        while r >= l:
            currwater = (r - l) * (min(heights[l], heights[r]))
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
            maxwater = max(currwater, maxwater)
        return maxwater



        