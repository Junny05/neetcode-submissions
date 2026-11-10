class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # k sized sliding sum, we want max of each k-sized sliding to be appended to max
        # we want to return amx which has max of each of the k-sized sliding window
        # L --> R we can check using r - l + 1
        # nums[l+1:r] l = 0 r = 
        # 
        l = 0
        q = deque()
        res = []
        
        # 1,2,1,0,4,2,6
        # L R
        for r in range(len(nums)):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()

            q.append(r)

            if r - l + 1 > k:
                l += 1
                
            if q[0] < l:
                q.popleft()
                
            if r - l + 1 == k:
                res.append(nums[q[0]])
        return res 

            