class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while (l < r):
            if numbers[r] + numbers[l] == target:
                return [l+1,r+1]
            else:
                sum = numbers[r] + numbers[l]
                if (sum > target):
                    r-=1
                else:
                    l+=1