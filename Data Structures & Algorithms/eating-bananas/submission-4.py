class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while hi > lo:
            k = lo + (hi-lo) // 2
            hours = sum(math.ceil(pile/k) for pile in piles)
            if hours <= h:
                hi = k
            else:
                lo = k + 1
        return lo