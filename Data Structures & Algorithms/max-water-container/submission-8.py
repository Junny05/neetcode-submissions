class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights) - 1
        l = 0
        maxheight = 0
        while r > l:
            currheight = (r-l) * min(heights[l], heights[r])
            if heights[r] >= heights[l]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            maxheight = max(currheight, maxheight)
        return maxheight



        