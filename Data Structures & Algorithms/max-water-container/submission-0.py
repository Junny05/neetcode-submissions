class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights) - 1
        l = 0
        curr_max = 0
        while r > l:
            curr_height = (r - l) * min(heights[l], heights[r])
            if heights[l] < heights[r]:
                l+=1
            elif heights[r] <= heights[l]:
                r-=1
            curr_max = max(curr_max, curr_height)
        return curr_max


        