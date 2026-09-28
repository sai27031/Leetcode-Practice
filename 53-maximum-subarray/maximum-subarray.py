class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        c_sum = 0
        for i in range(len(nums)):
            c_sum += nums[i]
            if c_sum > max_sum:
                max_sum = c_sum
            if c_sum<0:
                c_sum=0
        return max_sum