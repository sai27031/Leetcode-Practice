class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        dq = deque()
        left,right = 0,0
        while right<n:
            while dq and nums[right]>=nums[dq[-1]]:
                dq.pop()
            dq.append(right)
            if dq[0]<left:
                dq.popleft()
            if right+1>=k:
                result.append(nums[dq[0]])
                left += 1
            right += 1
        return result
