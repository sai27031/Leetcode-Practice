class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        temp = [-1]*n
        for i in range(n):
            if nums[i] > 0 and nums [i] <= n:
                temp[nums[i]-1] = 1
        for i in range(n):
            if temp[i] == -1:
                return i+1
        return n+1