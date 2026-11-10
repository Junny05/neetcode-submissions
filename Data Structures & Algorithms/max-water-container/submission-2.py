class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights) - 1
        l = 0
        currmax = 0 
        while r > l:
            currheight = (r - l) * min(heights[l], heights[r])
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
            currmax = max(currheight, currmax)
        return currmax


        