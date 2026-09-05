class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        min_len = n + 1
        curr_sum = 0
        for right in range(n):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return min_len if min_len != n+1 else 0




