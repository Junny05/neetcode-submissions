class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while r >= l:
            mid = l + (r-l) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] <= nums[r]:
                # 3 ,4 ,5 ,6 = mid , r = 1, 2, target = 1
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else: 
                    l = mid + 1
        if nums[l] == target: 
            return l
        else:
            return -1
