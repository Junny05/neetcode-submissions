class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set()

        for i in nums:
            if i not in sett:
                sett.add(i)
            else:
                return True
        return False