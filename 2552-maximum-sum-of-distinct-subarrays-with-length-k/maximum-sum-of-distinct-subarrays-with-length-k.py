class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        window = {}
        current_sum = 0
        left = 0
        for right in range(len(nums)):
            window[nums[right]] = window.get(nums[right] ,0) + 1
            current_sum += nums[right]

            if right - left + 1 > k:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                current_sum -= nums[left]
                left += 1
            if right - left + 1 == k and len(window) == k:
                max_sum = max(max_sum ,  current_sum)
        return max_sum