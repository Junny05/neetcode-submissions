class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxheight = 0
        while r > l:
            maxheight = max(maxheight, (r - l) * min(heights[l], heights[r]))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r-=1
        return maxheight
        
        