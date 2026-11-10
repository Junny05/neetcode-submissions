class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = sum(piles)
        res = 0

        while hi >= lo:
            mid = (lo + hi) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)
            if hours > h:
                lo = mid + 1
            else:
                res = mid
                hi = mid - 1
        return res