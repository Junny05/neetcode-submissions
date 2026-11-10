class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        res = []
        while r > l:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            else:
                sum1 = numbers[l] + numbers[r]
                if sum1 > target:
                    r-=1
                elif sum1 < target:
                    l+=1