class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check if n-1 in a hashmap, store each value in hashmap
        # have a O(1) lookup to see if its there if not, 
        # we move forward, if it is the start we can continue from there?
        
        myset = set(nums)
        res = 1
        length = 0
        
        if not myset:
            return 0

        for n in myset:
            if n-1 not in myset:
                length = 1 
                curr = n 
                while curr + 1 in myset:
                    length += 1
                    curr += 1
            res = max(length, res)
        return res
                